
class fontPageAction:
    def __init__(self,driver):
        self.driver=driver

    def click_show(self):
        self.driver.find_element_by_xpath('//*[@text="显示"]').click()

    def click_fontsize(self):
        self.driver.find_element_by_xpath('//*[@text="字体大小"]').click()

    def click_font_big(self):
        self.driver.find_element_by_xpath('//*[@text="大"]').click()

    def click_font_normal(self):
        self.driver.find_element_by_xpath('//*[@text="普通"]').click()


