from selenium import webdriver
from Selectors import Selectors
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random
import string


class CommonMethods():

    def __init__(self,driver):

        self.driver = driver


    def test_find_element(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        print("PASS: Element found")

    def test_click_javascript(self,locator):
        click_var = self.driver.find_element_by_css_selector(locator)
        self.driver.execute_script("arguments[0].click();", click_var)
        print("PASS: Element clicked")

    def test_find_list(self,locator,tag):
        html_list = self.driver.find_element_by_css_selector(locator)
        items = html_list.find_elements_by_tag_name(tag)
        for item in items:
            text = item.text
            print(text)



    def test_assert_text(self,text,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        assert text in element.text
        print(element.text)
        # try:
        #     assert text in element.text
        #     print("PASS: Text matches " + text)
        # except AssertionError:
        #     print("FAIL: Text does not match " + text)



    def test_iframe(self,iframe):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, iframe)))
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.switch_to.frame(element)
        print("PASS: Switched to iframe. ")



    def test_enter_text(self,locator,text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        element.send_keys(text)

    def test_press_enter(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element.send_keys(Keys.RETURN)

    def test_search_cache_invalidation(self,link):
            self.driver.get(link)
            search_results2 = self.driver.find_element_by_xpath("//p[@class='mod-filter-results__count']").text.split(" ")[3]
            print("After invalidating the cache the number of search results is : " + search_results2)
            if search_results2 >= str("1"):
                print("PASS: Invalidating the cache still shows results")
            else:
                print("FAILED: Invalidating the cache does not display results")



    def test_language_switch(self,link):
        url = self.driver.current_url
        if link == url:
            print("PASS: Language market switch works")
        else:
            print("FAILED: Language market switch did not work")



    def test_counter(self,locator,click):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        print(element.text)
        compare = element.text
        click_var = self.driver.find_element_by_css_selector(click)
        self.driver.execute_script("arguments[0].click();", click_var)
        after_click = int(element.text)
        print(after_click)
        if int(after_click) == int(compare)+int(1):
            print("it increased by one")

        else:
            print("it did not increase by one")


    def test_string(self):
        test =("https://www.nestle-cereals.com/global/en/fitness/inspirational-stories/pink-ribbon?")
        characters = '12345abcdefghij890'
        string2add = ''
        for i in range(1,7):
            string2add += random.choice(characters)
        print(string2add)
        web = str(test) + str(string2add)
        print(web)
        self.driver.get(web)

