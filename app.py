from node import binarynode
import os
from questions import isCity,welcome,frisAsk,isCountry,isGender,isMedals,isCategories,isAge,isCountry,isDeport,isPeople,option

# rootNode = binarynode('Que genero tienen quien gano la medalla de oro en natacion?','')
# rootNode.insertLeft('Cuantos anios tienes','18'

def __main__():
    os.system('cls')
    op = welcome()
    # listQues = [isGender('null'),isCountry('null'),isCity('null'),isMedals('null'),isDeport('null'),isAge('null'),isCategories('null')]
    
    cont = 0
    
    if op == 1:
        if frisAsk() == 2:
            lisAcction = []
            for n in range(0,7):
                if n == 0:
                    val = isGender('F')
                    lisAcction.append(val) 
                    
                if n == 1:
                    va= lisAcction[0][1]               
                    val = isCountry(va)
                    lisAcction.append(val)
                if n == 2:
                    val = lisAcction[1][1]
                    # print(f"{val[0]}")
                    vl = isCity(val[0])    
                    lisAcction.append(vl)

                if n == 3:
                    val = lisAcction[0][1]
                    val2 = lisAcction[1][1]
                    val3 = lisAcction[2][1]
                    
                    # print(f"{val3}")
                    isPeople(val,val2[0],val3[1])
                    op = option()
                    if op== 1:
                        print('\nCreo que eh adivinado ehehe!!')
                        break
                        
                cont = cont + 1
                if cont == 6:
                    break    
    else:
        print('Fin del Juego')
# def lisquest(id_pais,):
#     listQues = [isGender('null'),isCountry('null'),isCity('null'),isMedals('null'),isDeport('null'),isAge('null'),isCategories('null')]
    
if __name__ == "__main__":
    __main__()