from WebPage import *
from Address import Address

class Directorio(WebPage):
    def __init__(self, url):
        self.url = url
        self.log = Log("Directorio","./logs/Directorio.log")
        self.programName = "4. Directorio"

    def getAllMails(self):
        mailList = [f"{mail.get('href')}".replace("mailto:","",-1) for mail in self.soup.find_all("a", href=re.compile(r"^mailto:"))]
        mailList.sort()
        return mailList

    def mailToStr(self,mailList):
        mailListStr = ""
        for eachMail in mailList:
            mailListStr += f" - {eachMail}\n"
        return mailListStr

    def writeMailsToTxt(self, str):
        file = open("logs/directorio_emails.txt","w+")
        file.write(str)

    def countVowelsInList(self, list):
        vowels = ['a','e','i','o','u']
        count = 0
        for eachItem in list:
            if eachItem[0] in vowels:
                count += 1
        return count
    
    def getRawData(self):
        allAdresses = []
        for soupObj in self.soup.find_all(class_="tabla ancho100"):
            rawData = soupObj.find_all('td') 
        return rawData


    def run(self):
        self.start()

        mailList = self.getAllMails()
        mailListStr = self.mailToStr(mailList)
        self.writeMailsToTxt(mailListStr)
        print(f"Mails: {self.log.logIfThirty('writting file...')}")

        countMails = self.countVowelsInList(mailList)
        print(f"Count of mails: {countMails}")

        # data = self.countVowelsInList(self.getRawData())
        # print(f"Count of mails: {countMails}")
        self.getRawData()