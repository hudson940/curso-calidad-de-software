# using selenium scrap the number of active users and courses done

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest
from time import sleep

class eis_test(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_load(self):
        url = 'https://campusvirtualunillanos.co/'
        self.browser.get(url)
        activeUsers = self.browser.find_element(By.XPATH, '//section[@id="numbers"]//h3[1]')
        print('active users: %s' % activeUsers.text)
        coursesDone = self.browser.find_element(By.XPATH, '//div[@class="h-100 rate-box rate-box-2 bg-cloudburst"]/h3')
        print('courses done: %s' % coursesDone.text)

if __name__ == '__main__':
    unittest.main()