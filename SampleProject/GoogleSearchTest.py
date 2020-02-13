from selenium import webdriver
import unittest
import Report


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Drivers/chromedriver")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_search_automation(self):
        self.driver.get("https://www.google.com")

        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_class_name("hsuHs").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




if __name__ =='__main__':
    unittest.main(testRunner=Report.HTMLTestRunner(output='/Users/alexandru.mandache/PycharmProjects/cpw_smoke_test/Reports'))