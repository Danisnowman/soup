from WebPage import *
class CS(WebPage):

    def __init__(self, url):
        self.url = url
        self.log = Log("CS","./logs/CS.log")
        self.programName = "3. CS"

    def getFceLogo(self,className):
        image = self.soup.find("img", {"class": className })
        imagesStr = f"{image.get('src')}\n" 
        return imagesStr

    def getMeta(self, param):
        meta = ""
        for metaItem in self.soup.find_all("meta", property=f"og:{param}"):
            meta = f"{metaItem}\n"
        return meta

    def run(self):
        self.start()

        title = self.getTitle().text
        print(f"Title: {self.log.logIfThirty(title)}")

        titleLink = self.getLinkFromHref("fl-photo-content fl-photo-img-png")
        print(f"Title's Link: {self.log.logIfThirty(titleLink)}")

        fceLogo = self.getFceLogo("fl-photo-img wp-image-500 size-full")
        print(f"FCE's Logo: {self.log.logIfThirty(fceLogo)}")
    
        metaTitle = self.getMeta("title")
        print(f"Meta Title: {self.log.logIfThirty(metaTitle)}")

        metaOg = self.getMeta("description")
        print(f"Meta Description: {self.log.logIfThirty(metaOg)}")

        countA = self.countTag("a")
        print(f"Count all <a>: {countA} ")

        countDiv = self.countTag("div")
        print(f"Count all <div>: {countDiv} ")

