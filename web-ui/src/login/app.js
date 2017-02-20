/*
 * Copyright (c) 2017 ThoughtWorks, Inc.
 *
 * Pixelated is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Pixelated is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with Pixelated. If not, see <http://www.gnu.org/licenses/>.
 */

import React from 'react';
import { translate } from 'react-i18next';
import InputField from 'src/common/input_field/input_field';
import SubmitButton from 'src/common/submit_button/submit_button';

import './app.scss';

const errorMessage = (t, authError) => {
  if (authError) return <p className='error'>{t('error.auth')}</p>;
  return <div />;
};

export const App = ({ t, authError }) => (
  <div className='login'>
    <img className='logo' src='/public/images/logo-orange.svg' alt='Pixelated logo' />
    {errorMessage(t, authError)}
    <form className='standard' id='login_form' action='/login' method='post'>
      <InputField name='username' label={t('login.email')} />
      <InputField type='password' name='password' label={t('login.password')} />
      <SubmitButton buttonText={t('login.submit')} />
    </form>
  </div>
);

App.propTypes = {
  t: React.PropTypes.func.isRequired,
  authError: React.PropTypes.bool
};

export default translate('', { wait: true })(App);
