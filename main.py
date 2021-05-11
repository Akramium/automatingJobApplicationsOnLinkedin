from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os

# Environment variables
PATH = "/Development/chromedriver.exe"
LOGIN_URL = os.getenv("LOGIN_URL")
LINKEDIN_URL = os.getenv("LINKEDIN_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

# Chrome size 1920x1080 
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

# Login
driver.get(url=LOGIN_URL)
driver.find_element_by_name("session_key").send_keys(EMAIL)
driver.find_element_by_name("session_password").send_keys(PASSWORD)
driver.find_element_by_class_name("sign-in-form__submit-button").click()

# Get job list
driver.get(url=LINKEDIN_URL)
jobs = driver.find_elements_by_css_selector(".jobs-search-results__list .jobs-search-results__list-item")

for job in jobs:
    job.click()
    try:
        time.sleep(3)
        apply_job_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
        apply_job_button.click()
        print("Apply button clicked!")

        time.sleep(3)
        mobile_phone = driver.find_element_by_css_selector(".display-flex input")
        mobile_phone.clear()
        mobile_phone.send_keys(PHONE)
        print("Phone number typed")

        submit_application_button = driver.find_element_by_css_selector("footer button")
        if submit_application_button.text == "Submit application":
            time.sleep(3)
            # submit_application_button.click()
            print("Submit button clicked!")
            # pass
        else:
            time.sleep(3)
            close_button = driver.find_element_by_css_selector("#artdeco-modal-outlet svg")
            close_button.click()
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Close button clicked!")
    except NoSuchElementException:
        continue

