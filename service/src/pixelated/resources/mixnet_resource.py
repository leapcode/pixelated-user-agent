#
# Copyright (c) 2017 LEAP
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.

import json

from email.utils import parseaddr
from pixelated.resources import respond_json_deferred, BaseResource
from twisted.web import server
from twisted.logger import Logger
from txzmq import ZmqEndpoint, ZmqEndpointType
from txzmq import ZmqFactory, ZmqREQConnection

from leap.bitmask.core import ENDPOINT


class MixnetResource(BaseResource):
    # XXX: this is hacky, we should use bitmask.js properly in the web-ui
    #      But, if we and up doing zmq interface, we can do
    #      something more generic for all the API.

    isLeaf = True
    log = Logger()

    def render_GET(self, request):
        zf = ZmqFactory()
        e = ZmqEndpoint(ZmqEndpointType.connect, ENDPOINT)
        _conn = ZmqREQConnection(zf, e)

        _mail = self.mail_service(request)
        userid = _mail.account_email
        _, address = parseaddr(request.args.get('search')[0])

        def callback(resp_json):
            response = json.loads(resp_json[0])
            if response['error'] is not None:
                respond_json_deferred(response['error'], request, status_code=404)
            else:
                respond_json_deferred(response['result'], request, status_code=200)

        def err(fail):
            respond_json_deferred(str(fail), request, status_code=404)

        data = ["mail", "mixnet_status", userid, address]
        d = _conn.sendMsg(*data)
        d.addCallback(callback)
        d.addErrback(err)

        return server.NOT_DONE_YET
