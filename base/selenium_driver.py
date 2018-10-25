from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDrive:
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "name":
            return By.NAME
        if locatorType == "xpath":
            return By.XPATH
        if locatorType == "css":
            return By.CSS_SELECTOR
        if locatorType == "class":
            return By.CLASS_NAME
        if locatorType == "link":
            return By.LINK_TEXT

        else:
            print("Locator type" + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator: " + locator + " and LocatorType: " + locatorType)
        except:
            print("Element Found with locator: " + locator + " and LocatorType: " + locatorType)
        return element

    def
