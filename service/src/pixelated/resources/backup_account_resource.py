#
# Copyright (c) 2017 ThoughtWorks, Inc.
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

import os
import json

from twisted.python.filepath import FilePath
from twisted.web.http import OK, NO_CONTENT, INTERNAL_SERVER_ERROR
from twisted.web.server import NOT_DONE_YET
from twisted.web.template import Element, XMLFile, renderElement

from pixelated.resources import BaseResource
from pixelated.resources import get_protected_static_folder
from pixelated.account_recovery import AccountRecovery
from pixelated.support.language import parse_accept_language


class BackupAccountPage(Element):
    loader = XMLFile(FilePath(os.path.join(get_protected_static_folder(), 'backup_account.html')))

    def __init__(self):
        super(BackupAccountPage, self).__init__()


class BackupAccountResource(BaseResource):
    isLeaf = True

    def __init__(self, services_factory, authenticator, leap_provider):
        BaseResource.__init__(self, services_factory)
        self._authenticator = authenticator
        self._leap_provider = leap_provider

    def render_GET(self, request):
        request.setResponseCode(OK)
        return self._render_template(request)

    def _render_template(self, request):
        site = BackupAccountPage()
        return renderElement(request, site)

    def render_POST(self, request):
        account_recovery = AccountRecovery(
            self._authenticator.bonafide_session,
            self.soledad(request),
            self._service(request, '_leap_session').smtp_config,
            self._get_backup_email(request),
            self._leap_provider.server_name,
            language=self._get_language(request))

        def update_response(response):
            request.setResponseCode(NO_CONTENT)
            request.finish()

        def error_response(response):
            request.setResponseCode(INTERNAL_SERVER_ERROR)
            request.finish()

        d = account_recovery.update_recovery_code()
        d.addCallbacks(update_response, error_response)
        return NOT_DONE_YET

    def _get_backup_email(self, request):
        return json.loads(request.content.getvalue()).get('backupEmail')

    def _get_language(self, request):
        return parse_accept_language(request.getAllHeaders())
