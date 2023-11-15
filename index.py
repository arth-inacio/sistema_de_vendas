
from tkinter import *
from intro import Splash
from Usuariologin import Login
from Admin_menu import Admin

class Index_Principal(Splash, Login, Admin):
    def __init__(self) -> None:
        global b
        if b == 0:
            super().__init__()
            b = 1
        Login.__init__(self)
        self.loginwindow.mainloop()

        self.mainw = Toplevel(bg="black")
        width = 1000
        height = 600
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\favicon.ico')
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("Tobacco Realm")
        self.mainw.resizable(0, 0)
        self.getdetalhes()
           
    def getdetalhes(self) -> None:
        self.amontarmain()

    def amontarmain(self) -> None:
        self.admin_mainmenu(8,8)

if __name__=="__main__":
    b = 0
    w = Index_Principal()
    w.mainw.mainloop()