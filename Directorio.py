from WebPage import *

class Directorio(WebPage):
    def __init__(self, url):
        self.url = url
        self.log = Log("Directorio","./logs/Directorio.log")

    def run(self):
        self.start()