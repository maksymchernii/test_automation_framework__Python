from .base_page import BasePage
from .locators import MailPageLocator
from .locators import CollectMailLocator


class MailPage(BasePage):
    def should_be_mail_page(self):
        self.should_be_content()
        self.should_be_compose_button()
        self.should_be_login()

    def check_sending_mail(self, sending_mail):
        assert self.find_elements(CollectMailLocator.LIST_OF_INBOX) >= sending_mail, "Mail is not be present"

    def should_be_content(self):
        assert self.is_element_present(*MailPageLocator.MAIL_CONTENT), "login from is not be present"

    def should_be_compose_button(self):
        assert self.is_element_present(*MailPageLocator.MAIL_COMPOSE_BUTTON), "login email field is not be present"

    def should_be_login(self):
        assert self.is_element_present(*MailPageLocator.HERO_MAIL_LOCATOR), "login password field is not be present"

    def write_dict(self, len_selector, key_selector, values_selector):

        inboxes_mails = self.find_elements(len_selector)

        mails_keys = self.find_elements(key_selector)
        mails_keys_format = mails_keys

        mails_value = self.find_elements(values_selector)
        mails_value_format = mails_value

        mails_dict = {mails_keys_format[i].text: mails_value_format[i].text for i in range(0, len(inboxes_mails))}
        return mails_dict

    def send_logs(self, mails_dict):

        count = 0

        for elem in range(0, len(mails_dict)):
            alpha_in_mail = []
            digit_in_mail = []
            mail_on_theme = mails_dict.keys()[count]
            message_on_theme = mails_dict.values()[count]
            combine = mail_on_theme + message_on_theme
            for symb in combine:
                if symb.isdigit():
                    digit_in_mail.append(symb)

                if symb.isalpha():
                    alpha_in_mail.append(symb)

            res = "Received mail on theme {0} with message: {1}. " \
                  "It contains {2} letters and {3} numbers.\n". \
                format({mail_on_theme}, {message_on_theme}, {len(alpha_in_mail)}, {len(digit_in_mail)})

            count += 1

            self.enter_text(MailPageLocator.IFRAME_TEXTAREA, res)

    def get_logs_mail(self, checkbox_elements, logs_field_elements, remove_btn_locator):

        checkbox = self.find_elements(checkbox_elements)
        logs_field = self.find_elements(logs_field_elements)

        test_field = [logs_field[i].text for i in range(0, len(logs_field))]
        test = [checkbox[i] for i in range(0, len(checkbox))]

        count = 0
        for i in test:
            if "Logs" not in test_field[count]:
                i.click()
            count += 1

        remove_btn = self.find_element(remove_btn_locator)
        remove_btn.click()
