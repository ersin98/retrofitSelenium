class Deneme():
    def something(self,a):
        pass

    def otherthings(self,b):
        pass


    def runController(self,x,y):
        self.something(x)
        self.otherthings(y)

    def runControllerWithInput(self,x,writingArea,input,y):
        self.something(x)
        self.write(writingArea,input)
        self.otherthings(y)


    def runController(self,y,x,writingArea=None,input=None): 
        self.something(x) 
        if writingArea and input: 
            self.write(writingArea,input) 
        self.otherthings(y)