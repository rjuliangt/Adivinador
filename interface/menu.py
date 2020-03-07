from tkinter import Tk,TkVersion,Widget,LabelFrame,Label,messagebox,Frame,Button
from tkinter import messagebox as MS
# windows.iconbitmap('ruta')
# windows.config(bg="") 
# fram =Frame()
# fram.config(relief='sunken')
# fram.config(cursor='hand2')
def dos():
	# res = MS.askquestion("Pregunta!", )
	# Label(window,text=res).pack()
    fram.grid_remove()
    fm =LabelFrame(frame,text='Preguntas..',font=('Arial Bold',14))
    fm.grid(row = 2,column = 2,columnspan = 5, pady=10,padx=10)
    

# CadetBlue'
window = Tk()
window.title("Adivinador")
window.geometry('560x320')
window.resizable(0,0)
window.config(bg='black',pady=5,padx=5)
frame= Frame(window)

frame.pack()
frame.config(width=500,height=315)
title =Label(frame,foreground='black',text='\nSoy EL Adivinador De Medallistas\n OLIMPICOS :D',font=('Arial Bold', 14))
title.grid(row = 1, column = 4)
fram =LabelFrame(frame,text=' Instrucciones',font=('Arial Bold',14))
fram.grid(row = 2,column = 2   ,columnspan = 5, pady=10,padx=10)
msg = Label(fram, text='Este juego consiste en darle pistas al ente adivinadar para que\n \
    logre dar con el medallista en el que estas pensando, puedes salir del juego\n \
    presionando la letra "O", bueno empecemos\n',font=('Arial Bold', 11))
msg.grid(row = 3,column = 5,pady=15)
button = Button(frame,fg = 'white',bg = 'green', text='Comenzar!!',font=('Arial Bold', 14), command=dos)
button.grid(row = 5,column = 4,pady =10)
button.config(cursor='hand2')
button.config(width=12,height=2)
window.mainloop()



