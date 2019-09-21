from WebPage import *

class Portal(WebPage):

    def __init__(self, url):
        self.url = url
        self.log = Log("Portal","./logs/Portal.log")
        self.programName = "1. Portal"


    def getAddr(self):
        addr = self.soup.find("a", {"href": "#myModal"})
        return addr

    def getTel(self):
        tel = self.soup.find("a", {"href": "tel:+50223387700"})
        return tel

    def getMail(self):
        mail = self.soup.find("a", {"href": "mailto:inf@ufm.edu"})
        return mail

    def getMenuItems(self):
        menuItems = self.soup.find("table", {"id": "menu-table"})
        return menuItems

    def getHrefMIUButton(self, attr):
        href = [eachHref.get("href") for eachHref in self.soup.find_all('a', attrs={'href': re.compile(attr)})]
        return href
    
    def getAllImgHref(self):
        images = [image.get('src') for image in self.soup.find_all('img')]
        imagesStr = ""
        # imagesStr += [f"{image}\n" for image in images]
        for image in images:
            imagesStr += f" - {image}\n"
        return imagesStr


    def run(self):
        self.start()

        title = self.getTitle().text
        print(f"GET the title and print it: {self.log.logIfThirty(title)} ")
        
        
        address = self.getAddr().text
        print(f"GET the address and print it: {self.log.logIfThirty(address)} ")
        
        tel = self.getTel().text
        print(f"GET the telephone number and print it: {self.log.logIfThirty(tel)} ")

        mail = self.getMail().text
        print(f"GET the mail and print it: {self.log.logIfThirty(mail)} ")

        menuItems = self.getMenuItems().text
        print(f"GET the menu items and print it: {self.log.logIfThirty(menuItems)} ")

        href = f"{self.getHref()}\n"        
        print(f"GET the href and print it: {self.log.logIfThirty(href)} ")

        buttonHrefMIU = f'{self.getHrefMIUButton("auto&hd=ufm.edu")}'
        print(f"GET the href of the MIU button and print it: {self.log.logIfThirty(buttonHrefMIU)} ")

        buttonHrefMail = f'{self.getHrefMIUButton("ejemplo%40ufm.edu")}'
        print(f"GET the href of the MIU button and print it: {self.log.logIfThirty(buttonHrefMail)} ")

        images = f"{self.getAllImgHref()}\n"
        print(f"GET the href of all images and print it: {self.log.logIfThirty(images)} ")

        countA = self.countTag("a")
        print(f"Count all <a> and print it: {countA} ")