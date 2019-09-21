from WebPage import *

class Estudios(WebPage):
    
    def __init__(self, url):
        self.url = url
        self.log = Log("Estudios","./logs/Estudios.log")

    def navigate(self):
        href =  self.soup.find('div',{'class': "menu-key"})
        return href

    def displayItems(self):
        topMenuItems = ""
        for items in self.soup.find_all("div", {"id": "topmenu"}):
            for li in items.find_all("li"):
                topMenuItems += f" - {li.text}\n"
        return topMenuItems

    def getAllEstudios(self, className):
        estudios = ""
        for estudio in self.soup.find_all("div", {"class": className }):
            estudios += f" - {estudio.text}\n" 
        return estudios

    def getAllLi(self, className, insideParam):
        estudios = ""
        for estudio in self.soup.find_all("div", {"class": className }):
            for li in estudio.find_all(insideParam):
                estudios += f" - {li.text}\n" 
        return estudios



    def run(self):
        self.start()

        estudiosHref = f"{self.navigate()}"
        print(f"Navigate to /Estudios: {self.log.logIfThirty(estudiosHref)}")

        topMenuItem = self.displayItems()
        print(f"Top Menu Items: {self.log.logIfThirty(topMenuItem)}")

        estudios = self.getAllEstudios("estudios")
        print(f"Estudios: {self.log.logIfThirty(estudios)}")

        leftBarItems = self.getAllLi("leftbar","li")
        print(f"Estudios: {self.log.logIfThirty(leftBarItems)}")

        socialMedia = self.getLinkFromHref("social pull-right")
        print(f"Social Media: {self.log.logIfThirty(socialMedia)}")

        countA = self.countTag("a")
        print(f"Count all <a>'s and print it: {countA} ")

