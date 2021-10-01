class pow():
    def __init__(self,x,n):
        self.base=x
        self.power=n
    def printpow(self):
        print(self.base**self.power)
p=pow(2,3)
p.printpow()
