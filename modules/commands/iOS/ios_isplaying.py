class payload:
    def __init__(self):
        self.name = "isplaying"
        self.description = "view mediaplayer info"
        self.type = "native"
        self.id = 108

    def run(self,conn,server,command):
        return self.name
