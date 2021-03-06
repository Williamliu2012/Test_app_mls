from appium import webdriver


def initDriver():
    desired_caps = dict()
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5.1.1"
    desired_caps["deviceName"] = "127.0.0.1:62025"
    desired_caps["appPackage"] = "com.android.settings"
    desired_caps["appActivity"] = ".Settings"
    desired_caps["resetKeyboard"] = True
    desired_caps["unicodeKeyboard"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver