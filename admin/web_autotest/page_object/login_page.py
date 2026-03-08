from selenium.webdriver.common.by import By

from admin.web_autotest.page_object.base_page import BasePage
from admin.web_autotest.utils.log_util import logger


class LoginPage(BasePage):
    """登陆页面：用户登录"""
    _BASE_URL = "http://192.168.243.50:8080"

    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")

    def login(self):
        logger.info("登陆页面：用户登录")
        logger.info("访问登陆页面")
        self.do_send_keys("admin123", self.__INPUT_USERNAME)
        self.do_send_keys("admin123", self.__INPUT_PASSWORD)
        self.do_find(self.__BTN_LOGIN).click()

        #->首页
        from admin.web_autotest.page_object.home_page import HomePage
        return HomePage(self.driver)