import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from Selectors import Selectors
from CommonMethods import CommonMethods
import unittest
import Report
import self as self
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

class MiscTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        # cls.driver.get("https://www.nestle-cereals.com/global/en/fitness/inspirational-stories/pink-ribbon?")
        # cls.driver.implicitly_wait(10)

        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        cls.driver = webdriver.Chrome(chrome_options=chrome_option,
                                      executable_path="/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Drivers/chromedriver")
        cls.driver.get("https://nestle-cereals.com/uk")
        cls.driver.implicitly_wait(10)


    def test_01_click_cookie_popup(self):
        locator = Selectors.selectors["de_close_popup"]
        CommonMethods.test_click_javascript(self,locator)
        print("clicked element")


    def test_02_pledge_counter(self):
        locator = Selectors.selectors["pledge_counter_bgd"]
        locator2 = Selectors.selectors["pledge_counter_active_class"]
        click = Selectors.selectors["click_pledge_counter"]
        CommonMethods.test_string(self)
        CommonMethods.test_find_element(self,locator)
        CommonMethods.test_counter(self,locator2,click)

    def test03_sticky_buy_now(self):
        locator = Selectors.selectors["sticky_buy_now"]
        locator2 = Selectors.selectors["nutrition_facts"]
        self.driver.get("https://www.nestle-cereals.com/master01/en/brands/products/qa-product-page-do-not-delete")
        CommonMethods.test_find_element(self,locator2)
        CommonMethods.test_click_javascript(self,locator)
        print("am dat click pe ala")
        time.sleep(10)








    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=Report.HTMLTestRunner(output='/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Reports'))