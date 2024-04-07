from base import BasePage

class CancelLeave(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def cancel_leave(self,note):
        self.find_element("xpath", "//a[text()='My Leave']").click()
        leave_path="//div[contains(text(),'{}')]/parent::div/following-sibling::div/div/li/button".format(note)
        self.find_element("xpath",leave_path).click()
        self.sleep_for_seconds()
        self.find_element("xpath", "//p[text()='View Leave Details']").click()
        length = len(self.find_elements("xpath", "//button[text()=' Cancel ']"))
        for i in range(length):
            self.find_elements("xpath", "//button[text()=' Cancel ']")[i].click()
            self.sleep_for_seconds()
