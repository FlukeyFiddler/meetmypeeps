from selenium import webdriver
import unittest


class LandingPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_loads(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Meet My Poops', self.browser.title)


if __name__ == '__main__':
    unittest.main()
