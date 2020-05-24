import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, find_dotenv

currentDirectory = os.path.dirname(os.path.abspath(__file__))
env_path = currentDirectory + '/../.env'
load_dotenv(dotenv_path=env_path)


class Main():

    def __init__(self):
        chromeOptions = Options()
        #chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--disable-notifications')
        pathChromeDriver = os.path.dirname(os.path.abspath(__file__)) + '/../drivers/chromedriver'
        self.browser = webdriver.Chrome(executable_path=pathChromeDriver, chrome_options=chromeOptions)
        self.browser.set_window_size(1920,1080)
        self.browser.set_window_position(0,0)

    def openSite(self, url):
        self.browser.get(url)

    def loginFacebook(self):
        self.browser.find_element_by_id('email').send_keys(os.getenv("USERNAME_FB"))
        self.browser.find_element_by_id('pass').send_keys(os.getenv("PASSWORD_FB"))
        sleep(1)
        self.browser.find_elements_by_css_selector("input[data-testid=royal_login_button]")[0].send_keys(Keys.ENTER)

    def writePost(self, msg):
        try:
            postBox = self.browser.find_element_by_xpath("//*[@name='xhpc_message']")
        except:
            postBox = self.browser.find_element_by_class_name('_5rpu')
        postBox.click()
        postBox.send_keys(msg)
        self.browser.find_elements_by_css_selector("button._1mf7")[0].click()

    def getTextBible(self):
        import json
        from random import randint
        with open(currentDirectory + '/../assets/bibleVerses.json') as jsonFile:
            listBibleVerses = json.load(jsonFile)
        verse = listBibleVerses[randint(0, len(listBibleVerses)-1)]
        verseToPost = "{}\n{}".format(verse['text'], verse['ref'])
        return verseToPost

if __name__ == "__main__":    
     
    main = Main()
    main.openSite('https://facebook.com')
    main.loginFacebook()
    main.writePost(main.getTextBible())
    sleep(3)
    main.browser.quit()