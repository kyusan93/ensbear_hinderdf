import time
from pathlib import Path

import os

os.system('wmic process where name="chrome.exe" delete')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def start_driver():
    op = webdriver.ChromeOptions()
    op.add_argument("user-data-dir=C:\\Users\\Jonathan\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
    op.add_experimental_option("excludeSwitches", ["enable-logging"])
    ser = Service("C:\\Tools\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=op)
    delete_cache(driver)
    return driver

def delete_cache(driver):
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    driver.switch_to.window(driver.window_handles[0])  # Switch Selenium controls to the original tab to continue normal functionality.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter

def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    actions.perform()
    driver.quit()

if __name__ == '__main__':
    driver = start_driver()
