from selenium import webdriver
from Selectors import Selectors
from CommonMethods import CommonMethods
import unittest
import HtmlTestRunner
import self as self
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://nestle-cereals.com/uk")
        cls.driver.implicitly_wait(10)

    def test_01(self):
        locator = Selectors.changeLater["popup"]

        CommonMethods.test_find_element(self, locator)
        print("test page")

    def test_02(self):
        print("Am ajuns la testul 2!!!")

    def test_03(self):
        print("Am ajuns la testul 3 !!!!!")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
