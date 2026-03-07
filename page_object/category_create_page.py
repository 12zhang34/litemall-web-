from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage
from utils.log_util import logger
from utils.web_util import click_execption


class CategoryCreatePage(BasePage):
    __INPUT_CATEGORY_ID = (By.XPATH, "//*[text()='商品编号']/..//*[@class='el-input__inner']")
    __INPUT_CATEGORY_NAME = (By.XPATH, "//*[text()='商品名称']/..//*[@class='el-input__inner']")
    __BTN_CONFIRM = (By.XPATH, "//*[text()='上架']")

    """创建商品"""
    def create_category(self, category_id, category_name):
        logger.info("创建类目页面：创建类目")
        self.do_send_keys(category_id, self.__INPUT_CATEGORY_ID)
        self.do_send_keys(category_name, self.__INPUT_CATEGORY_NAME)
        WebDriverWait(self.driver, 10).until(click_execption(*self.__BTN_CONFIRM))
        from page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)