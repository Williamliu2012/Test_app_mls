

class searchPageAction:
    def __init__(self,driver):
        self.driver=driver

    def click_search(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()

    def input_value(self):
        self.driver.find_element_by_id('android:id/search_src_text').send_keys('我爱中华')

    def click_back(self):
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()
