from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from utils.log_util import logger


class LoginPage(BasePage):
    """登陆页面：用户登录"""
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/"

    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")

    def login(self):
        logger.info("登陆页面：用户登录")
        logger.info("访问登陆页面")
        self.do_send_keys("hogwarts", self.__INPUT_USERNAME)
        self.do_send_keys("test12345", self.__INPUT_PASSWORD)
        self.do_find(self.__BTN_LOGIN).click()

        #->首页
        from page_object.home_page import HomePage
        return HomePage(self.driver)