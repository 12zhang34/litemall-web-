from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage
from utils.log_util import logger


class CategoryListPage(BasePage):

    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, "//*[text()='创建成功']")
    __MSG_DELETE_OPERATE = (By.XPATH, "//*[text()='删除成功']")


    def click_add(self):
        logger.info("商品列表页面：点击添加")
        self.do_find(self.__BTN_ADD).click()

        from page_object.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    def get_operate_result(self):
        logger.info("商品列表页面：添加操作结果")
        # element = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        # # self.driver.refrash_window()
        # msg = element.text
        # return msg

    def delete_category(self, category_name):
        logger.info("商品列表页面：删除操作")
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        #->还是当前页
        return CategoryListPage(self.driver)

    def get_delete_result(self):
        logger.info("商品列表页面：删除操作结果")
        # element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE)
        # # self.driver.refrash_window()
        # msg = element.text
        # logger.info(f"冒泡消息是{msg}")
        # return msg