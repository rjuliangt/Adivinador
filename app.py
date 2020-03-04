from node import binarynode

rootNode = binarynode('Que genero tienen quien gano la medalla de oro en natacion?','')

rootNode.insertLeft('Cuantos anios tienes','18')


def printQuestion(menssage):
    val = int(input("{}".format(menssage)))
    return val

def __main__():
    n = printQuestion("Que genero tienen quien gano la medalla de oro en natacion?")
    print("Inicio de Juego")
    print("Pregunta: {}".format(rootNode.question))
    print("Respuesta {}".format(rootNode.answer))
    print("\nleft: {}".format(rootNode.left_children.question))
    print("Respuesta {}".format(rootNode.left_children.answer))
    

if __name__ == "__main__":
    __main__()