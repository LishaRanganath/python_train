from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base import BasePage
from selenium import webdriver

class Leave(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def leave_page(self,link1,link2):
        self.driver.find_element(By.XPATH,link1).click();
        self.sleep_for_seconds()
        self.driver.find_element(By.XPATH, link2).click();
        self.sleep_for_seconds()

    def apply_leave_page(self,from_date,to_date):
        self.driver.find_elements(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")[0].click();
        self.sleep_for_seconds()
        self.driver.find_element(By.XPATH, "//div[@role='option']/child::span[text()='CAN - FMLA']").click()
        self.sleep_for_seconds()
        self.driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")[0].send_keys(from_date)
        self.sleep_for_seconds()
        leave_till=self.driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")[1]
        self.sleep_for_seconds()
        leave_till.send_keys(Keys.COMMAND + 'a')
        leave_till.send_keys(Keys.DELETE)
        self.sleep_for_seconds()
        leave_till.send_keys(to_date)
        self.sleep_for_seconds()
        self.driver.find_elements(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")[1].click()
        self.driver.find_element(By.XPATH,"//div[@class='oxd-select-option']/child::span[text()='End Day Only']").click()
        self.sleep_for_seconds(4)
