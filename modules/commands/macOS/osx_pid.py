class payload:
    def __init__(self):
        self.name = "pid"
        self.description = "get process id"
        self.type = "native"
        self.id = 122

    def run(self,conn,server,command):
        return self.name
