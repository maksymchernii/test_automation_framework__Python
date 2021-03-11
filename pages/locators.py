from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".form")
    LOGIN_EMAIL = (By.ID, "id-l")
    LOGIN_PASSWORD = (By.ID, "id-p")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button")


class MailPageLocator():
    MAIL_COMPOSE_BUTTON = (By.CSS_SELECTOR, ".default")
    MAIL_CONTENT = (By.CSS_SELECTOR, ".default")
    HERO_MAIL_LOCATOR = (By.CSS_SELECTOR, ".login")
    SEND_TO_INPUT = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[1]/div[1]/div[4]/input[2]")
    THEME_LETTER_INPUT = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[1]/div[4]/div[2]/input")
    IFRAME_TEXTAREA = (By.ID, "tinymce")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//div/button[@class='default send']")
    MAIL_SEND_ALERT = (By.CSS_SELECTOR, ".sendmsg__ads-ready")
    WRITE_AGAIN = (By.CSS_SELECTOR, "button.default:nth-child(3)")
    RETURN_TO_INBOX = (By.CSS_SELECTOR, "button.action:nth-child(4)")


class CollectMailLocator():
    LIST_OF_INBOX = (By.XPATH, "//*/td/a[@class='msglist__row_href']")
    KEYS = (By.CSS_SELECTOR, "tr > td.msglist__row-subject > a")
    VALUES = (By.XPATH, "//tbody/tr/td[@class='msglist__row-subject']/a/strong")
    MAILS_COUNT = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section/table/tbody/tr")
    CHECKBOX = (By.CSS_SELECTOR, "tr > td > label > input[type='checkbox']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "a[class='controls-link remove']")

