
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
        inputList = []
        for symbol in inputSymbols:
            inp = float(input(symbol + ": "))
            inputList.append(inp)
        return inputList


    def f1_k(self): 
        inputValues = self.f1TakeInputs(["Vp", "p", "μ"])
        k = inputValues[0]**2 * inputValues[1] - (4/3) * inputValues[2]
        print('%.5f'%k)


    def f1_p(self): 
        inputValues = self.f1TakeInputs(["k", "μ", "vp"])
        p = (inputValues[0] + (4/3) * inputValues[1]) / inputValues[2]**2 
        print('%.5f'%p)

    def f1_u(self): 
        inputValues = self.f1TakeInputs(["vp", "p", "k"])
        u = (inputValues[0] ** 2 * inputValues[1] - inputValues[2]) / (4 / 3)
        print('%.5f'%u)

    def f1_vp(self): 
        inputValues = self.f1TakeInputs(["k", "u", "p"])
        vp = ((inputValues[0] + (4 / 3) * inputValues[1]) / inputValues[2]) ** 0.5
        print('%.5f'%vp)