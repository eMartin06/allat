class Állat:
        def __init__(self,allat,suly):
            self.allat = allat
            self.suly = suly
    
állatfaj=[]
for _ in range(3):
    allatka=input('Add meg egy állatfaj nevét! ')
    sulyucska=int(input('Hány kilogramm a tömege egy példánynak? '))
    állatfajok= Állat(allatka,sulyucska)
    állatfaj.append(állatfajok)

for a in állatfaj:
    print('A(z)',a.allat,'tömege',a.suly,'kg')