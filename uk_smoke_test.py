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

class Uk_smoke_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        # cls.driver.get("https://nestle-cereals.com/uk")
        # cls.driver.implicitly_wait(10)

        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        cls.driver = webdriver.Chrome(chrome_options=chrome_option,
                                      executable_path="/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Drivers/chromedriver")
        cls.driver.get("https://nestle-cereals.com/uk")
        cls.driver.implicitly_wait(10)

    def test_01(self):
        locator = Selectors.selectors["popup"]

        CommonMethods.test_find_element(self, locator)
        print("test page")

    def test_02_click_cookie_popup(self):
        locator = Selectors.selectors["close_popup"]
        CommonMethods.test_click_javascript(self,locator)
        print("clicked element")

    def test_03_find_main_logo(self):
        locator = Selectors.selectors["main_logo"]
        CommonMethods.test_find_element(self,locator)

    def test_04_main_menu(self):
        locator = Selectors.selectors["main_menu_list"]
        tag = "li"
        CommonMethods.test_find_list(self,locator,tag)

    def test_05_latest_content(self):
        locator = Selectors.selectors['latest_content']
        CommonMethods.test_find_element(self,locator)

    def test_06_footer_scroller(self):
        locator = Selectors.selectors['brand_scroller_footer']
        CommonMethods.test_find_element(self,locator)

    def test_07_write_us_text(self):
        locator = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['write_us_text']
        CommonMethods.test_assert_text(self,text,locator)


    def test_08_faq(self):
        locator = Selectors.selectors['footer_faq_icon']
        locator2 = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['faq_text']
        CommonMethods.test_click_javascript(self,locator)
        CommonMethods.test_assert_text(self,text,locator2)


    def test_09_in_person(self):
        locator = Selectors.selectors['footer_in_person_icon']
        locator2 = Selectors.selectors['footer_active_talk_section']
        text = Selectors.text_to_assert['in_person_text']
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_assert_text(self, text, locator2)


    def test_10_footer_logo(self):
        locator = Selectors.selectors['footer_logo']
        CommonMethods.test_find_element(self,locator)

    def test_11_product_page(self):
        self.driver.get("https://www.nestle-cereals.com/uk/en/products-promotions/brands/lion-brand/lion-cereal?sefgsgsg")
        locator = Selectors.selectors['click_adimo_cta']
        iframe = Selectors.selectors['admimo_switch_to_iframe']
        text = Selectors.text_to_assert['adimo_text']
        locator2 = Selectors.selectors['adimo_assertion_css']
        CommonMethods.test_click_javascript(self,locator)
        CommonMethods.test_iframe(self,iframe)
        CommonMethods.test_assert_text(self,text,locator2)


    def test_12_recipe_page(self):
        self.driver.get("https://www.nestle-cereals.com/uk/en/recipes-tips/recipes/rainbow-jars?sefgsgsg")
        locator = Selectors.selectors['click_adimo_cta']
        iframe = Selectors.selectors['admimo_switch_to_iframe']
        text = Selectors.text_to_assert['adimo_text']
        locator2 = Selectors.selectors['adimo_assertion_css']
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_iframe(self, iframe)
        CommonMethods.test_assert_text(self, text, locator2)

    def test_13_brand_page(self):
        self.driver.get("https://www.nestle-cereals.com/uk/en/products-promotions/brands/cheerios-brand?sefgsgsg")
        locator = Selectors.selectors['click_adimo_cta']
        iframe = Selectors.selectors['admimo_switch_to_iframe']
        text = Selectors.text_to_assert['adimo_text']
        locator2 = Selectors.selectors['adimo_assertion_css']
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_iframe(self, iframe)
        CommonMethods.test_assert_text(self, text, locator2)

    def test_14_bazaarvoice_page1(self):
        self.driver.get("https://www.nestle-cereals.com/uk/en/products-promotions/brands/lion-brand/lion-cereal?sefgsgsg'")
        locator = Selectors.selectors["click_bazaarvoice"]
        text = Selectors.text_to_assert["bazaarvoice_text"]
        locator2 = Selectors.selectors['bazaarvoice_assertion']
        CommonMethods.test_click_javascript(self,locator)
        CommonMethods.test_assert_text(self,text,locator2)

    def test_15_bazaarvoice_page2(self):
        self.driver.get("https://www.nestle-cereals.com/uk/en/products-promotions/brands/lion-brand/lion-cereal?sefgsgsg'")
        locator = Selectors.selectors["click_bazaarvoice"]
        text = Selectors.text_to_assert["bazaarvoice_text"]
        locator2 = Selectors.selectors['bazaarvoice_assertion']
        CommonMethods.test_click_javascript(self, locator)
        CommonMethods.test_assert_text(self, text, locator2)

    def test_16_search(self):
        locator = Selectors.selectors["search_icon_click"]
        CommonMethods.test_click_javascript(self,locator)
        text = Selectors.text_to_assert["search_text"]
        locator2 = Selectors.selectors['search_imput_text']
        CommonMethods.test_enter_text(self,locator2,text)
        CommonMethods.test_press_enter(self,locator2)
        time.sleep(3)

    def test_17_cache_invalidation(self):
        link = Selectors.selectors["uk_link_cache"]
        CommonMethods.test_search_cache_invalidation(self,link)





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=Report.HTMLTestRunner(output='/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Reports'))