from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Set options
options = ChromeOptions()
options.headless = False

#driver settings
driver = webdriver.Chrome(options=options)
driver.maximize_window

class Driver:
    def __init__(self, driver):
        self.driver = driver

    # Rerun in dock
    def rerun(self, x, y):
        for _ in range(x):
            y()

    # Waiting time for webdriver to perform further action
    def wait(self, x):
        return WebDriverWait(self.driver, x)
