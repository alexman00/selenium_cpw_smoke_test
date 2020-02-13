from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProject.POMDemo.Pages.LoginPage import LoginPage
from SampleProject.POMDemo.Pages.HomePage import HomePage
import Report

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(
            executable_path="/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Drivers/chromedriver")

        cls.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        #
        #
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #
        # self.driver.find_element_by_id("btnLogin").click()
        #
        # self.driver.find_element_by_class_name("panelTrigger").click()
        # print("yup")
        #
        # self.driver.find_element_by_link_text("Logout").click()

        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=Report.HTMLTestRunner(output='/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Reports'))