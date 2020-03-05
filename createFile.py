import os.path as path

def creationFile():
    if path.exists("logs.txt"):
        print('Si existe')
    else:
        print('No existe')
        file = open("logs.txt", "tx")
        file.close()

def insertQuestion(ques,answ):
    file = open('logs.txt','a')
    pos = file.tell() #obtenems poscicion del puntero
    file.seek(pos) #posicionamos el puntero
    file.write(f'\n{ques}? \n {answ}')
    print(f'{pos}')
    print(file.tell())
    file.close()

creationFile()
insertQuestion('Hola?','Dimesese')