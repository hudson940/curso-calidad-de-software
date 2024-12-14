from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest
from re import sub
from decimal import Decimal

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		urlGeneral = 'https://capibaraeventos.com/shop/'
		urls = ['producto-1', 'producto-2', 'producto-3']

		for url in urls:
			print("Resultado -> %s" % url)
			print("%s%s" % (urlGeneral, url))
			self.browser.get("%s%s" % (urlGeneral, url))
			numberList = self.browser.find_elements(By.CLASS_NAME, 'oe_currency_value')
			res = []
			for number in numberList:
				if number.text:
					res.append(number.text)
			
			self.assertGreater(len(res), 0, msg='Fallo, no se encontro el precio en el resultado de -> %s' % (url))
			self.assertGreater(Decimal(sub(r'[^\d.]', '', res[0])), 0, msg='Fallo, el precio del producto debe ser mayor a 0')

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()