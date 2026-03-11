def click_execption(by, element, attempts=5):
    def _inner(driver):
        """
        多次点击同个按钮
        :param driver:
        :return:
        """
        count = 0 # 实际循环次数
        while count<attempts:
            try:
                count +=1
                # 因为点击的过程可能出现报错，所以需要添加try 捕获报错的异常
                driver.find_element(by, element).click()
                return True
            except Exception:
                print("出现异常")
        return False
    return _inner