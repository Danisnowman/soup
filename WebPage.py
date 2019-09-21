from bs4 import BeautifulSoup
from Log import Log
import requests,sys,csv,json
import re

class WebPage:
    url = None
    soup = None
    html_content = None
    hrefs = ""
    log = None

    def start(self):
        print("==========================")
        self.parse()

    def parse(self):
        try:
            self.html_content = requests.get(self.url).text
        except:
            print(f"unable to get {self.url}")
            sys.exit(1)
        # Parse the html content, this is the Magic ;)
        self.soup = BeautifulSoup(self.html_content, "html.parser")

    def getTitle(self):
        return self.soup.title
    
    def getHref(self):
        for href in self.soup.find_all(href=True):
            self.hrefs += f" - {href}\n"
        return self.hrefs   

    def countTag(self, param):
        count = len(self.soup.find_all(param))
        return count


    def getLinkFromHref(self, className):
            estudios = ""
            for estudio in self.soup.find_all("div", {"class": className }):
                for link in estudio.find_all("a"):
                    estudios += f" - {link.get('href')}\n" 
            return estudios
    

    def getSOUP(self):
        return self.soup