#!/usr/bin/env python

import os, unittest

from selenium import webdriver


class TestOpenSite(unittest.TestCase):

    def setUp(self):
        os.environ['DISPLAY'] = ":0"
        self.path = os.path.dirname(os.path.abspath(__file__)) + '/../drivers/geckodriver'
        self.browser = webdriver.Firefox(executable_path=self.path)

    def testTitle(self):
        self.browser.get('http://www.google.com/')
        self.assertIn('Google', self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)