import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_SUCCESS = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_PLUS = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_CREATED_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_DELETE_BTN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/div/div[1]/div[1]/button[2]""")
    LOCATOR_POSTS = (By.XPATH, """//*[@id="app"]/main/div/div[3]/div[1]""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_MAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_CONTACT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD, time=3)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD, time=3)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        logging.info(f"Start finding error text in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")

        return error_field.text

    def login_success(self):
        logging.info("Start find success text")
        success_field = self.find_element(TestSearchLocators.LOCATOR_SUCCESS, time=3)
        text = success_field.text
        logging.info(f"We find text {text} is login field {TestSearchLocators.LOCATOR_SUCCESS[1]}")
        return text

    def click_plus_post_button(self):
        logging.info("Click plus post button")
        self.find_element(TestSearchLocators.LOCATOR_PLUS).click()

    def input_title(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE, time=3)
        title_field.clear()
        title_field.send_keys(word)

    def input_description(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION, time=3)
        description_field.clear()
        description_field.send_keys(word)

    def input_content(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT, time=3)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_button(self):
        logging.info("Click 'save' button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()
        time.sleep(3)

    def post_success(self):
        logging.info("Start find post title")
        success_post = self.find_element(TestSearchLocators.LOCATOR_CREATED_TITLE, time=3)
        text = success_post.text
        logging.info(f"We find post title -> {text} from {TestSearchLocators.LOCATOR_CREATED_TITLE[1]} ")
        return text

    def click_delete_btn(self):
        logging.info("Click delete post button")
        self.find_element(TestSearchLocators.LOCATOR_DELETE_BTN).click()
        time.sleep(3)

    def success_delete(self):
        logging.info("Start find list of posts")
        posts = self.find_element(TestSearchLocators.LOCATOR_POSTS, time=3)
        text = posts.text
        return text

    def click_contact_btn(self):
        logging.info("Click 'contact' button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def input_name(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD, time=3)
        name_field.clear()
        name_field.send_keys(word)

    def input_mail(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_MAIL_FIELD[1]}")
        mail_field = self.find_element(TestSearchLocators.LOCATOR_MAIL_FIELD, time=3)
        mail_field.clear()
        mail_field.send_keys(word)

    def input_contact_content(self, word):
        logging.info(f"Send {word} to the element {TestSearchLocators.LOCATOR_CONTENT_CONTACT[1]}")
        contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT, time=3)
        contact_field.clear()
        contact_field.send_keys(word)

    def click_contact_us_btn(self):
        logging.info("Click 'contact us' button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def alert(self):
        logging.info("Start find alert")
        alert = self.driver.switch_to.alert
        text = alert.text
        return text