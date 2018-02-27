# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re
#from Automation_Frameworks.UI_Selenium_framework.Common_utils import model

class MaysRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.macys.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_mays_registration(self):
        print("=======Inside registration page======")
        self.driver.get(self.base_url )
        #click elemantsign in
        SigninlinkID = "globalMastheadSignIn"
        CreateProfileID = "createProfileContainer"

        self.driver.find_element_by_id(SigninlinkID).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(CreateProfileID).click()
        driver = self.driver


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
