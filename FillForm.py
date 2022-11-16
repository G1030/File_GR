import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Fillform:
    driver=webdriver.Chrome()

    def fill_form(self, url):
        # Get the Data
        email="govind@gmail.com"
        pass_word="Govind"

        # Get the XPATH / ID / Class
        email_xpath ="//input[@id='email']"
        pass_xpath ="//input[@id='pass']"
        login_button_xpath ="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button"
        try:
            # open the webpage
            self.driver.get(url)

            # find the XPATH of the HTML element present on the webpage
            email_xpath = self.driver.find_element(by=By.XPATH, value=email_xpath)
            pass_xpath = self.driver.find_element(by=By.XPATH, value=pass_xpath)
            login_button_xpath = self.driver.find_element(by=By.XPATH, value=login_button_xpath)

            # fill the HTML form
            email_xpath.send_keys(email)
            pass_xpath.send_keys(pass_word)
            time.sleep(5)

            # click on the Submit button
            login_button_xpath.click()
        except:
            print("ERROR : XPATH not found !")

f=Fillform()
url="https://www.facebook.com/"
f.fill_form(url)

