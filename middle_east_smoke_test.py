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

class Middle_east_smoke_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        # cls.driver.get("https://nestle-cereals.com/me/en/homepage")
        # cls.driver.implicitly_wait(10)

        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        cls.driver = webdriver.Chrome(chrome_options=chrome_option,
                                      executable_path="/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Drivers/chromedriver")
        cls.driver.get("https://nestle-cereals.com/me/en/homepage")
        cls.driver.implicitly_wait(10)




    def test_01_find_main_logo(self):
        locator = Selectors.selectors["main_logo"]
        CommonMethods.test_find_element(self,locator)

    def test_02_main_menu(self):
        locator = Selectors.selectors["main_menu_list"]
        tag = "li"
        CommonMethods.test_find_list(self,locator,tag)


    def test_03_latest_content(self):
        locator = Selectors.selectors['latest_content']
        CommonMethods.test_find_element(self,locator)

    def test_04_footer_scroller(self):
        locator = Selectors.selectors['brand_scroller_footer']
        CommonMethods.test_find_element(self,locator)

    def test_05_write_us_text(self):
        locator = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['write_us_text']
        CommonMethods.test_assert_text(self,text,locator)


    def test_06_faq(self):
        locator = Selectors.selectors['footer_faq_icon']
        locator2 = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['faq_text']
        CommonMethods.test_click_javascript(self,locator)
        CommonMethods.test_assert_text(self,text,locator2)


    def test_07_in_person(self):
        locator = Selectors.selectors['footer_in_person_icon']
        locator2 = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['in_person_text']
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_assert_text(self, text, locator2)


    def test_08_footer_logo(self):
        locator = Selectors.selectors['footer_logo']
        CommonMethods.test_find_element(self,locator)



    def test_09_search(self):
        locator = Selectors.selectors["search_icon_click"]
        CommonMethods.test_click_javascript(self,locator)
        text = Selectors.text_to_assert["search_text"]
        locator2 = Selectors.selectors['search_imput_text']
        CommonMethods.test_enter_text(self,locator2,text)
        CommonMethods.test_press_enter(self,locator2)


    def test_10_cache_invalidation(self):
        link = Selectors.selectors["me_link_cache"]
        CommonMethods.test_search_cache_invalidation(self,link)
        time.sleep(1)


    def test_11_product1(self):
        self.driver.get("https://www.nestle-cereals.com/me/en/products-promotions/brands/honey-cheerios?sgsgs")
        locator = Selectors.selectors["de_fusepump_cta_product"]
        locator2 = Selectors.selectors["de_fusepump_iframe"]
        locator3 = Selectors.selectors["muli_country_flag_click"]
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_click_javascript(self,locator3)
        CommonMethods.test_iframe(self, locator2)


    def test_12_product2(self):
        self.driver.get("https://www.nestle-cereals.com/me/en/products-promotions/brands/chocapic?Sgsg")
        locator = Selectors.selectors["de_fusepump_cta_product"]
        locator2 = Selectors.selectors["de_fusepump_iframe"]
        locator3 = Selectors.selectors["muli_country_flag_click"]
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_click_javascript(self,locator3)
        CommonMethods.test_iframe(self, locator2)


    def test_13_language_switch(self):
        self.driver.get("https://www.nestle-cereals.com/me/en/homepage?Sgsg")
        locator = Selectors.selectors["language_switch"]
        locator2 = Selectors.selectors["choose_arabic"]
        link = Selectors.selectors["arabic_homepage"]
        CommonMethods.test_click_javascript(self,locator)
        CommonMethods.test_click_javascript(self,locator2)
        CommonMethods.test_language_switch(self,link)






    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=Report.HTMLTestRunner(output='/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Reports'))