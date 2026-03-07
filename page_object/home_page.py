from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from utils.log_util import logger


class HomePage(BasePage):

    __MENU_MALL_MANAGE = (By.XPATH, "//*[text()='商品管理']")
    __MENU_PRODUCT_CATEGORY = (By.XPATH, "//*[text()='商品列表']")

    """系统首页"""
    def go_to_category(self):
        logger.info("系统页面：进入商品类目")
        #点击菜单，商场管理
        self.do_find(self.__MENU_MALL_MANAGE).click()
        #点击商品列表
        self.do_find(self.__MENU_PRODUCT_CATEGORY).click()

        from page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
