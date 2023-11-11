
from tkinter import *
from intro import Splash
from Usuario import Login
from Admin_menu import Admin

class Index_Principal(Splash, Login, Admin):
    def __init__(self) -> None:
        global b
        if b == 0:
            super().__init__()
            b = 1
        Login.__init__(self)
        self.loginwindow.mainloop()

        self.mainwindow = Toplevel(bg="black")
        width = 800
        height = 600
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainwindow.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\favicon.ico')
        self.mainwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainwindow.title("Tobacco Realm")
        self.mainwindow.resizable(0, 0)
        self.getdetalhes()
           
    def getdetalhes(self) -> None:
        self.amontarmain()

    def amontarmain(self) -> None:
        self.admin_mainmenu(8,8)

if __name__=="__main__":
    b = 0
    w = Index_Principal()
    w.mainwindow.mainloop()