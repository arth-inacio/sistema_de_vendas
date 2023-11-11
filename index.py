from tkinter import ttk
from tkinter import *
from intro import Splash
from Usuario import Login

class Index_Principal(Splash, Login):
    def __init__(self) -> None:
        global b
        if b == 0:
            super().__init__()
            b = 1
        Login.__init__(self)
        self.loginwindow.mainloop()
        self.mainwindow.TopLevel(bg="black")
        width = 1350
        height = 700
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainwindow.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\favicon.ico')
        self.mainwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainwindow.resizable(0, 0)
           

if __name__=="__main__":
    b = 0
    w = Index_Principal()
    w.mainwindow.mainloop()