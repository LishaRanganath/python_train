from selenium import webdriver
from login import Login
from leave_navigate import Leave
class HRM:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(7)
        self.login_page=Login(self.driver)
        self.apply_leave=Leave(self.driver)

    def login(self,username,password):
        self.login_page.login_user(username,password)

    def logout(self):
        self.login_page.logout_user()

    def leave(self,link1,link2):
        self.apply_leave.leave_page(link1,link2)

    def applying_leave_(self,from_date,to_date):
        self.apply_leave.apply_leave_page(from_date,to_date)

    def duration(self,days,duration):
        self.apply_leave.day_and_duration(days,duration)

    def comments(self,note):
        self.apply_leave.comments(note)

hrm = HRM()
hrm.login("Admin", "admin123")
link1="//a[@class='oxd-main-menu-item']/child::span[text()='Leave']"
link2="//a[text()='Apply']"
hrm.leave(link1,link2)
hrm.applying_leave_('2024-05-04','2024-07-04')
hrm.duration("End Day","Half Day")
hrm.comments("2 days leave")
hrm.logout()
