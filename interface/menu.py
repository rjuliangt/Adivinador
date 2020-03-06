from tkinter import *

windows = Tk()
# window = tk.PanedWindow

windows.title("Adivinador")
windows.geometry('600x450')
title = Label(windows,bg="black" ,foreground='white',text="SOY EL ADIVINADOR DE MEDALLISTAS\n OLIMPICOS :D",font=("Arial Bold", 18)).place(x=80,y=10)
instru = Label(windows, text="Este juego consiste en darle pistas al ente adividar para que\n \
    logre dar con el medallista en el que estas pensando, puedes salir del juego\n \
    presionando la letra 'O', bueno empecemos",font=("Arial Bold", 12)).place(x=15,y=90)
windows.mainloop()