from selenium.webdriver import Keys

from base import BasePage
from cancel import CancelLeave

class Leave(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def leave_page(self,link1,link2):
        self.find_element("xpath",link1).click();
        self.sleep_for_seconds()
        self.find_element("xpath", link2).click();
        self.sleep_for_seconds()

    def apply_leave_page(self,from_date,to_date):
        self.find_elements("xpath", "//div[@class='oxd-select-text--after']//i")[0].click();
        self.sleep_for_seconds()
        self.find_element("xpath", "//div[@role='option']/child::span[text()='CAN - FMLA']").click()
        self.sleep_for_seconds()
        self.find_elements("xpath", "//input[@placeholder='yyyy-dd-mm']")[0].send_keys(from_date)
        self.sleep_for_seconds()
        leave_till=self.find_elements("xpath", "//input[@placeholder='yyyy-dd-mm']")[1]
        self.sleep_for_seconds()
        leave_till.send_keys(Keys.CONTROL + 'a')
        leave_till.send_keys(Keys.BACKSPACE)
        self.sleep_for_seconds()
        leave_till.send_keys(to_date)
        self.sleep_for_seconds()
        self.find_element("xpath", "//div[@class='orangehrm-card-container']").click()

    def day_and_duration(self,days,duration):
        self.find_elements("xpath", "//div[@class='oxd-select-text--after']//i")[1].click()
        days_path="//div[@class='oxd-select-option']/child::span[contains(text(),'{}')]".format(days)
        self.find_element("xpath",days_path).click()
        self.sleep_for_seconds()
        self.find_elements("xpath", "//div[@class='oxd-select-text--after']//i")[2].click()
        duration_path = "//div[@class='oxd-select-option']/child::span[contains(text(),'{}')]".format(duration)
        self.find_element("xpath", duration_path).click()
        self.sleep_for_seconds()


    def comments(self,note):
        self.find_element("xpath", "//textarea").send_keys(note)
        self.find_element("xpath", "//button[@type='submit']").click()
        self.sleep_for_seconds()

        cancel_page = CancelLeave(self.driver)
        cancel_page.cancel_leave(note)
