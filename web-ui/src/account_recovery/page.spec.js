import { shallow } from 'enzyme';
import expect from 'expect';
import React from 'react';

import { Page } from 'src/account_recovery/page';
import Header from 'src/common/header/header';
import Footer from 'src/common/footer/footer';

import AdminRecoveryCodeFormWrapper from './admin_recovery_code_form/admin_recovery_code_form';
import UserRecoveryCodeFormWrapper from './user_recovery_code_form/user_recovery_code_form';
import NewPasswordFormWrapper from './new_password_form/new_password_form';
import BackupAccountStepWrapper from './backup_account_step/backup_account_step';

describe('Account Recovery Page', () => {
  let page;
  let pageInstance;

  beforeEach(() => {
    const mockTranslations = key => key;
    page = shallow(<Page t={mockTranslations} />);
    pageInstance = page.instance();
  });

  it('renders account recovery page title', () => {
    expect(page.props().title).toEqual('account-recovery.page-title');
  });

  it('renders header without logout button', () => {
    expect(page.find(Header).props().renderLogout).toEqual(false);
  });

  it('renders footer', () => {
    expect(page.find(Footer).length).toEqual(1);
  });

  it('saves user code', () => {
    pageInstance.saveUserCode({ target: { value: '123' } });
    expect(pageInstance.state.userCode).toEqual('123');
  });

  it('prevents default event before next', () => {
    const eventSpy = expect.createSpy();
    pageInstance.nextStep({ preventDefault: eventSpy });

    expect(eventSpy).toHaveBeenCalled();
  });

  context('main content', () => {
    it('renders admin recovery code form as default form', () => {
      expect(page.find(AdminRecoveryCodeFormWrapper).length).toEqual(1);
      expect(page.find(UserRecoveryCodeFormWrapper).length).toEqual(0);
      expect(page.find(NewPasswordFormWrapper).length).toEqual(0);
    });

    it('renders user recovery code form when admin code submitted', () => {
      pageInstance.nextStep();

      expect(page.find(UserRecoveryCodeFormWrapper).length).toEqual(1);
    });

    it('returns to admin code form on user code form back link', () => {
      pageInstance.nextStep();
      pageInstance.previousStep();

      expect(page.find(AdminRecoveryCodeFormWrapper).length).toEqual(1);
    });

    it('renders new password form when user code submitted', () => {
      pageInstance.nextStep();
      pageInstance.nextStep();

      expect(page.find(NewPasswordFormWrapper).length).toEqual(1);
    });

    it('returns to user code form on new password form back link', () => {
      pageInstance.nextStep();
      pageInstance.nextStep();
      pageInstance.previousStep();

      expect(page.find(UserRecoveryCodeFormWrapper).length).toEqual(1);
    });

    it('renders backup account form after submitting new password', () => {
      pageInstance.nextStep();
      pageInstance.nextStep();
      pageInstance.nextStep();

      expect(page.find(BackupAccountStepWrapper).length).toEqual(1);
    });
  });
});
