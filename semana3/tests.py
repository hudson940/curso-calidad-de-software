import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebScrapingAndForms(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_google_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Selenium")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Selenium", driver.page_source)

    def test_fill_github_signup_form(self):
        driver = self.driver
        driver.get("https://github.com/join")
        self.assertIn("Join GitHub", driver.title)
        username = driver.find_element_by_id("user_login")
        email = driver.find_element_by_id("user_email")
        password = driver.find_element_by_id("user_password")
        username.send_keys("testuser")
        email.send_keys("testuser@example.com")
        password.send_keys("password123")
        self.assertIn("Create your account", driver.page_source)

    def test_fill_twitter_signup_form(self):
        driver = self.driver
        driver.get("https://x.com/i/flow/signup")
        self.assertIn("Sign up for Twitter", driver.title)
        name = driver.find_element_by_name("name")
        phone = driver.find_element_by_name("phone_number")
        name.send_keys("testuser")
        phone.send_keys("1234567890")
        self.assertIn("Create your account", driver.page_source)

    def test_fill_facebook_signup_form(self):
        driver = self.driver
        driver.get("https://www.facebook.com/r.php")
        self.assertIn("Sign up for Facebook", driver.title)
        firstname = driver.find_element_by_name("firstname")
        lastname = driver.find_element_by_name("lastname")
        email = driver.find_element_by_name("reg_email__")
        password = driver.find_element_by_name("reg_passwd__")
        firstname.send_keys("Test")
        lastname.send_keys("User")
        email.send_keys("testuser@example.com")
        password.send_keys("password123")
        self.assertIn("Create a new account", driver.page_source)

    def test_fill_linkedin_signup_form(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/signup")
        self.assertIn("LinkedIn", driver.title)
        email = driver.find_element_by_id("email-address")
        password = driver.find_element_by_id("password")
        email.send_keys("testuser@example.com")
        password.send_keys("password123")
        self.assertIn("Join LinkedIn", driver.page_source)

if __name__ == "__main__":
    unittest.main()