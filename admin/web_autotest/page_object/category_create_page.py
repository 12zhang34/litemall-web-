from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from admin.web_autotest.page_object.base_page import BasePage
from admin.web_autotest.utils.log_util import logger
from admin.web_autotest.utils.web_util import click_execption


class CategoryCreatePage(BasePage):
    __INPUT_CATEGORY_ID = (By.XPATH, "//*[text()='商品编号']/..//*[@class='el-input__inner']")
    __INPUT_CATEGORY_NAME = (By.XPATH, "//*[text()='商品名称']/..//*[@class='el-input__inner']")
    __BTN_CONFIRM = (By.XPATH, "//*[text()='上架']")
    __ERROR_MSG = (By.XPATH, "//div[contains(@class, 'el-message') and contains(text(),'已存在')]")

    def create_category(self, category_id, category_name):
        logger.info("创建类目页面：创建类目")

        # 1. 等待弹窗中的输入框可见（确保弹窗已出现）
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.__INPUT_CATEGORY_ID)
        )

        # 2. 用 JavaScript 直接设置商品编号（无需重试，永远不过期）
        id_input = self.do_find(*self.__INPUT_CATEGORY_ID)
        self.driver.execute_script("arguments[0].value = arguments[1];", id_input, category_id)

        # 3. 用 JavaScript 直接设置商品名称
        name_input = self.do_find(*self.__INPUT_CATEGORY_NAME)
        self.driver.execute_script("arguments[0].value = arguments[1];", name_input, category_name)

        # 4. 触发 input 事件（如果前端框架需要）
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", id_input)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", name_input)

        # 5. 快速检查是否有错误提示（例如编号已存在）
        try:
            error_elem = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.__ERROR_MSG)
            )
            raise AssertionError(f"创建失败，错误提示: {error_elem.text}")
        except TimeoutException:
            pass  # 无错误，继续

        # 6. 点击确认按钮
        WebDriverWait(self.driver, 10).until(click_execption(*self.__BTN_CONFIRM))

        from admin.web_autotest.page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)