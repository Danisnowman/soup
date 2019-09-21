from WebPage import *

class Estudios(WebPage):
    
    def __init__(self, url):
        self.url = url
        self.log = Log("Estudios","./logs/Estudios.log")

    def navigate(self):
        for eachHref in self.soup.find_all('a',attrs={'href': re.compile("ufm.edu/index.php/Estudios")}):
            href = eachHref
        return href

    def run(self):
        self.start()

        estudiosHref = f"{self.navigate()}"
        print(f"Navigate to /Estudios: {self.log.logIfThirty(estudiosHref)}")

