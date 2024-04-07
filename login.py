import time
from base import BasePage

class Login(BasePage):
        def __init__(self,driver):
            super().__init__(driver)

        def login_user(self,username,password):
            self.launch("https://opensource-demo.orangehrmlive.com/")
            self.find_element("name", "username").send_keys(username)
            self.sleep_for_seconds()
            self.find_element("name", "password").send_keys(password)
            self.sleep_for_seconds()
            self.find_element("xpath", "//button[@type='submit']").click()
            self.sleep_for_seconds()

        def logout_user(self):
            self.find_element("xpath","//span[@class='oxd-userdropdown-tab']").click()
            self.sleep_for_seconds()
            self.find_element("xpath","//ul[@class='oxd-dropdown-menu']/li/a[text()='Logout']").click()
            self.sleep_for_seconds(4)