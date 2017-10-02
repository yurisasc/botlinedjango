from selenium import webdriver
import unittest
import time

class NewVisitortest(unittest.TestCase):
    def setUp(self):
            self.browser = webdriver.Chrome('./chromedriver.exe')
    
    def tearDown(self):
            self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
            self.browser.get('http://www.google.com/xhtml')
            time.sleep(5)

            search_box = self.browser.find_element_by_name('q')
            search_box.send_keys('Gunung Agung')
            search_box.submit()
            time.sleep(5)
            self.assertIn('Bali',self.browser.page_source)

if __name__ == '__main__':#
	unittest.main(warnings='ignore')#
