from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class Splash:
    def __init__(self):
        self.splashwindow = Tk()
        self.splashwindow.title("Splash Screen")
        width = 900
        height = 670
        self.splashwindow.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\favicon.ico')
        self.splashwindow.config(bg="green")

        tela_largura = self.splashwindow.winfo_screenwidth()
        tela_altura = self.splashwindow.winfo_screenheight()
        x = (tela_largura / 2) - (width / 2)
        y = (tela_altura / 2) - (height / 2)
        self.splashwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.splashwindow.resizable(0, 0)
        path = "images/intro.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashwindow, width=890, height=560, bg="black", relief="sunken", bd=0)
        main.place(x=55, y=70)
        foto_frame = LabelFrame(main, width=420, height=440, bg="green", relief="raised", bd=0)
        foto = Label(foto_frame, image=img)
        foto.place(x=6, y=6)
        foto_frame.place(x=10, y=100)

        Label(main, text="SISTEMA DE VENDAS", font="Arial 20 bold", bg="white", fg="white").place(x=450, y=100)
        
        # Mensagem initial
        self.splashwindow.mainloop()
