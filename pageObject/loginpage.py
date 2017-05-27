#coding=utf-8
from selenium.webdriver.common.by import By
from basepage import BasePage

class LoginPage(BasePage):
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'password')
    submit_loc = (By.ID,'dologin')
    span_loc = (By.CSS_SELECTOR,'div.error-tt>p')
    dynpw_loc = (By.ID,'lbDynPw')
    userid_loc = (By.ID,'spnUid')

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def show_span(self):
        return self.find_element(*self.span_loc).text

    def seich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    def show_userid(self):
        return self.find_element(*self.userid_loc).text
