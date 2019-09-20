import logging

class Log:
    appName = None
    logger = None
    hdlr = None
    logPath = None
    formatter = None

    def __init__(self, appName="log", logPath=f"./logs/log.log"):
        self.appName = appName
        self.logPath = logPath
        self.logger = logging.getLogger(self.appName)
        self.hdlr = logging.FileHandler(self.logPath)
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr) 
        self.logger.setLevel(logging.WARNING)


    def logErr(self, err):
        self.logger.error(err)

    def getCheckIfThirty(self, lines):
        return (len(lines.split('\n')) > 30)

    def logIfThirty(self, lines):
        if self.getCheckIfThirty(lines):
            self.logErr(lines)
            return f"Output exceeds 30 lines, logging into {self.logPath}\n--------------------------"
        else:
            return f"{lines}\n --------------------------"



        