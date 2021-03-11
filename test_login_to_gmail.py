from .pages.login_page import LoginPage
from .pages.mail_page import MailPage
from .pages.locators import LoginPageLocators
from .pages.locators import MailPageLocator
from .pages.locators import CollectMailLocator
from .logics.logic import RandomText
from selenium.webdriver.common.by import By


def test_login_to_gmail(browser):

    login_link = "https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout"
    account_link = ""
    email = "demolink_test_post@ukr.net"
    password = "demolinkparole"
    logic = RandomText()
    message_count = 15

    signin_page = LoginPage(browser, login_link)
    mail_page = MailPage(browser, account_link)

    # LogIn Page
    signin_page.open()
    signin_page.should_be_login_email_page()
    signin_page.enter_text(LoginPageLocators.LOGIN_EMAIL, email)
    signin_page.enter_text(LoginPageLocators.LOGIN_PASSWORD, password)
    signin_page.click_on_the_element(LoginPageLocators.LOGIN_BUTTON)
    signin_page.find_element(MailPageLocator.HERO_MAIL_LOCATOR, time=1)

    # Mail Page
    mail_page.should_be_mail_page()
    mail_page.click_on_the_element(MailPageLocator.MAIL_COMPOSE_BUTTON)

    def send_message():
        mail_page.enter_text(MailPageLocator.SEND_TO_INPUT, email)
        mail_page.enter_text(MailPageLocator.THEME_LETTER_INPUT, logic.get_message(10))
        mail_page.go_to_frame(1)
        mail_page.enter_text(MailPageLocator.IFRAME_TEXTAREA, logic.get_message(10))
        mail_page.go_to_parent_window()
        mail_page.click_on_the_element(MailPageLocator.SEND_MESSAGE_BUTTON)
        mail_page.is_element_present(*MailPageLocator.MAIL_SEND_ALERT)

    for inbox in range(message_count - 1):
        send_message()
        mail_page.click_on_the_element(MailPageLocator.WRITE_AGAIN)
    else:
        send_message()
        mail_page.click_on_the_element(MailPageLocator.RETURN_TO_INBOX)

    mail_page.should_be_mail_page()
    mail_page.check_sending_mail(message_count)

    mails_dict = mail_page.write_dict(
        CollectMailLocator.MAILS_COUNT,
        CollectMailLocator.KEYS,
        CollectMailLocator.VALUES
    )

    mail_page.click_on_the_element(MailPageLocator.MAIL_COMPOSE_BUTTON)
    mail_page.enter_text(MailPageLocator.SEND_TO_INPUT, email)
    mail_page.enter_text(MailPageLocator.THEME_LETTER_INPUT, "Logs")
    mail_page.go_to_frame(1)

    mail_page.send_logs(mails_dict)

    mail_page.go_to_parent_window()
    mail_page.click_on_the_element(MailPageLocator.SEND_MESSAGE_BUTTON)
    mail_page.is_element_present(*MailPageLocator.MAIL_SEND_ALERT)
    mail_page.click_on_the_element(MailPageLocator.RETURN_TO_INBOX)

    mail_page.get_logs_mail(
        CollectMailLocator.CHECKBOX,
        CollectMailLocator.MAILS_COUNT,
        CollectMailLocator.REMOVE_BUTTON
    )

