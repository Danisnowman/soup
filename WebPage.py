from bs4 import BeautifulSoup
import requests,sys,csv,json

class WebPage:
    url = None
    soup = None
    html_content = None

    def start(self):
        self.parse()

    def parse(self):
        try:
            self.html_content = requests.get(self.url).text
        except:
            print(f"unable to get {self.url}")
            sys.exit(1)
        # Parse the html content, this is the Magic ;)
        self.soup = BeautifulSoup(self.html_content, "html.parser")
        


    def getSOUP(self):
        return self.soup