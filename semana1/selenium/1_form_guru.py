from selenium import webdriver
from selenium.webdriver.common import keys, by
import unittest
from time import sleep

class FormGuru(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_load(self):
        browser = self.browser
        browser.get("http://demo.guru99.com/test/login.html")
        fname = browser.find_element(by.By.ID, 'email')
        fname.clear()
        fname.send_keys('Anderson')
        lname = browser.find_element(by.By.ID, 'passwd')
        lname.clear()
        lname.send_keys('David')
        submitButton = browser.find_element(by.By.ID, 'SubmitLogin')
        submitButton.send_keys(keys.Keys.ENTER)
        sleep(2)
        res = browser.find_element(by.By.XPATH, '//html/body/div[2]/div/div/h3')
        self.assertEqual('Successfully Logged in...', res.text)

    def tearDown(self):
        print()

if __name__ == '__main__':
    unittest.main()