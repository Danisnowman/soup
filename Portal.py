from WebPage import *

class Portal(WebPage):

    def __init__(self, url):
        self.url = url
        self.log = Log("Portal","./logs/Portal.log")

    def run(self):
        self.start()

        title = f"{self.getTitle()}\n"
        print(f"GET the title and print it: {self.log.logIfThirty(title)} ")
        
        print(f"GET the href and print it: {self.log.logIfThirty(self.getHref())} ")

        # for div in self.soup.find_all("div"):
        #     print(div)
        #     print("--------------------------")
    