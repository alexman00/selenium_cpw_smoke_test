from selenium import webdriver
from Selectors import Selectors
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class CommonMethods():

    def __init__(self,driver):

        self.driver = driver



    def test_cookie_popup(self,locator):
        try:
            self.driver.find_element_by_id(locator)
            print("PASS: Cookie popup was found")
        except NoSuchElementException():
            print("FAIL: No such element exception for the cookie selector")
        except TimeoutException():
            print("FAIL: Timeout exception for the cookie selector")


    # def test_click_css(self,locator):
    #     self.driver.find_element_by_css_selector(locator).click()
    #
    # def test_click_class(self,locator):
    #     self.driver.find_element_by_class(locator).click()
    #
    # def test_click_id(self,locator):
    #     self.driver.find_element_by_id(locator).click()

    # wait for element to appear, then hover it
    def test_find_element(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        print("PASS: Element found")





