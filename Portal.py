from WebPage import WebPage

class Portal(WebPage):

    def __init__(self, url):
        self.url = url

    def run(self):
        self.start()
        print(self.soup)
        for div in self.soup.find_all("div"):
            print(div)
            print("--------------------------")