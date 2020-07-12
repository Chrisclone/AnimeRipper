from seleniumwire import webdriver
from getter import getter
import time
import os
import requests as r

class construct:
    def __init__(self, location, page):

        if location == "":
            location = r"C:\Users\clone\Desktop"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        options.add_argument('--disable-extensions')
        options.add_argument("--incognito")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--headless")
        options.add_argument("--log-level=OFF")

        self.parser = webdriver.Chrome(executable_path=r"C:\Users\clone\Desktop\chromedriver.exe", chrome_options=options)
        self.page = self.parser.get(page)

        name = ""
        for letter in self.fileName():
            if letter != ":" and letter !="\\":
                name += letter

        self.location = os.path.join(location, name + ".mp4") #Creates file name & location
        time.sleep(5)

        site = self.siteGetter()
        header = self.headerGetter()

        self.parser.quit()

        self.properRipper(site, header, page, self.location)


    def fileName(self):
        name = str(self.parser.find_element_by_class_name("information").text).split("\n")
        real = ""

        for i in name:
            real += i + " "

        return real

    def siteGetter(self):
        for reqs in self.parser.requests:
            if ".cdn." in str(reqs.path):
                return reqs.path

    def headerGetter(self):
        for reqs in self.parser.requests:
            if ".cdn." in str(reqs.path):
                return reqs.headers

    def properRipper(self, site, header, referer, location):
        getter(site, header, referer, location)

