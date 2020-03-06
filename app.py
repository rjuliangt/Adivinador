from node import binarynode
from questions import *

# rootNode = binarynode('Que genero tienen quien gano la medalla de oro en natacion?','')
# rootNode.insertLeft('Cuantos anios tienes','18')

def __main__():
    op = welcome()
    if op == 1:
        if frisAsk() == 2:
            # qes_an =
            isMedals()            
            # root = binarynode(qes_an[0],qes_an[1])
            # print('{} {}'.format(root.question,root.answer))
            isCountry()
            isGender()
            isCity()
          
        else:
            print(f'{type(askNameCountry())}')
            print('Fin del Juego')

if __name__ == "__main__":
    __main__()