from tkinter import *
from PIL import ImageTk, Image


class Splash:
    def __init__(self) -> None:
        self.splashmainw = Tk()
        self.splashmainw.title("Tobacco Realm")
        width = 1000
        height = 680

        self.splashmainw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')

        self.splashmainw.config(bg="darkgreen")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura / 2 ) - (width /2 )
        y = (tela_altura / 2 ) - (height /2 )
        self.splashmainw.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.splashmainw.resizable(0,0)
        path ="images/intro.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashmainw, width=890, height=560, bg="black", relief="sunken", bd="0")
        main.place(x=55,y=70)
        fotoframe = LabelFrame(main, width=420, height=444, bg="black", relief="raised", bd="0")
        foto=Label(fotoframe,image=img)
        foto.place(x=6,y=6)
        fotoframe.place(x=10,y=100)

        Label(main, text="Tobacco Realm", font="roboto 28 bold underline", bg="white", ).place(x=45, y=10)
        Label(main, text="Arthur", font="roboto 32 bold", bg="lightgreen").place(x=450, y=160)
        Label(main, text="Desenvolvedor Python", font="roboto 16 bold", bg="white").place(x=450, y=310)
        Label(main, text="Email : arthur.inacio08@gmail.com", font="roboto 16 bold", bg="white").place(x=445+5, y=360)
        
        self.splashmainw.mainloop()
