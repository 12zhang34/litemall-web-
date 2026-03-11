from datetime import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_autotest.admin.utils.driver_factory import get_driver


class BasePage:

    _BASE_URL = ""

    def __init__(self, base_driver = None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = get_driver()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def to_finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None, timeout=10):
        if locator:
            loc = (by, locator)
        else:
            loc = by
        ele = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(loc)
        )
        ele.clear()
        ele.send_keys(value)

    def do_quit(self):
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time.time())
        # 前提-在当前路径需要有一个images 文件夹
        file_path = f"./images/screenshot_{timestamp}.png"
        self.driver.save_screenshot(file_path)
        allure.attach.file(file_path, name="pic",
                           attachment_type=allure.attachment_type.PNG)

    def wait_element_until_visible(self, locator: tuple):
        return WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located(locator))