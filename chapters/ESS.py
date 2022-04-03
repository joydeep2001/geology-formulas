
class ESS:
    def __init__(self):
        print('Chosse a formula')
        print('1: Vp = √((k+4/3μ)/p)')
        formulaNumber = int(input())
        if formulaNumber == 1:
            self.f1()
    
    #Vp = √((k+4/3μ)/p)
    def f1(self):
        print("Press u for μ")
        unknownTerm = input("Enter the unknow term: ")
        unknownTerm = unknownTerm.lower()

        if unknownTerm == "k":
            self.f1_k()
        elif unknownTerm == "p":
            self.f1_p()
        elif unknownTerm == "u":
            self.f1_u()
        elif unknownTerm == "vp":
            self.f1_vp()
        else:
            print("invalid symbol!")
    
    def f1TakeInputs(self, inputSymbols):
        inputList = {}
        for symbol in inputSymbols:
            val = float(input(symbol + ": "))
            inputList[symbol] = val
        return inputList


    def f1_k(self): 
        vp, p, u = self.f1TakeInputs(["Vp", "p", "u"]).values()
        k = vp ** 2 * p - (4/3) * u
        print('%.5f'%k)


    def f1_p(self): 
        k, u, vp = self.f1TakeInputs(["k", "u", "Vp"]).values()
        p = (k + (4/3) * u) / vp ** 2 
        print('%.5f'%p)

    def f1_u(self): 
        vp, p, k = self.f1TakeInputs(["Vp", "p", "k"]).values()
        u = (vp ** 2 * p - k) / (4 / 3)
        print('%.5f'%u)

    def f1_vp(self): 
        k, u, p = self.f1TakeInputs(["k", "u", "p"])
        vp = ((k + (4 / 3) * u) / p) ** 0.5
        print('%.5f'%vp)