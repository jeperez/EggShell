class payload:
    def __init__(self):
        self.name = "screenshot"
        self.description = "take screenshot"
        self.type = "download"
        self.id = 109

    def run(self,conn,server,command):
        return self.name
