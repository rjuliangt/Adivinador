from node import binarynode
import os
from questions import isCity,welcome,frisAsk,isCountry,isGender,isMedals,isCategories,isAge,isCountry,isDeport 

# rootNode = binarynode('Que genero tienen quien gano la medalla de oro en natacion?','')
# rootNode.insertLeft('Cuantos anios tienes','18')

def __main__():
    os.system('cls')
    op = welcome()

    listQues = ["isGender,isCountry,isCity,isMedals,isDeport"]
    finish = False
    while finish != True:
        if op == 1:
            if frisAsk() == 2:
            # qes_an =     
            # root = binarynode(qes_an[0],qes_an[1])
            # print('{} {}'.format(root.question,root.answer))
                listQues[0]
    else:
   
        print('Fin del Juego')

if __name__ == "__main__":
    __main__()