

class player:

    def __init__(self,l):
        self.l = l
        self.fit = sum(self.l)
        self.eval = True#we eval every time

    def print(self):
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")
        print("fit: ",self.fit)
        for i in self.l:
            print(i,end="")
        print()
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")

    def hello(self):
        print("hello worl")


