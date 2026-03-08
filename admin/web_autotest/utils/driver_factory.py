
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver(headless: bool = False):
    chrome_options = Options()

    # 关闭 Chrome 保存密码弹窗
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 关闭密码泄露检测
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")

    # 关闭保存密码气泡
    chrome_options.add_argument("--disable-save-password-bubble")

    # 关闭通知弹窗
    chrome_options.add_argument("--disable-notifications")

    # 无痕模式
    chrome_options.add_argument("--incognito")

    # 防止自动化被部分网站识别（可选）
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Linux 环境下有时更稳定（可选）
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 无头模式（按需开启）
    if headless:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    driver.maximize_window()

    return driver