from tkinter import *
from Intro import Splash
from Userlogin import Login
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
        self.mainw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("Tobacco Realm")
        self.mainw.resizable(0, 0)
        self.getdetalhes()
           
    def getdetalhes(self) -> None:
        self.amontarmain()

    def amontarmain(self) -> None:
        #Aqui fica o nome no topo da pagina
        self.admin_mainmenu(8,8)
        self.topframe = LabelFrame(self.mainw, width=900, height=80, bg="black")
        self.topframe.place(x=50, y=5)
        self.loja_name = "Tobacco Realm"
        self.lable_loja = Label(self.topframe, text=self.loja_name, bg="black", justify="center")
        self.lable_loja.config(font="Roboto 30 bold", fg="snow")
        self.lable_loja.place(x=300, y=15)
        
        img = PhotoImage(file="images/perfil1.png")
        img = img.subsample(4, 4)
        self.meu_perfil = Label(self.topframe, image=img, compound=TOP)
        self.meu_perfil.image = img
        self.meu_perfil.place(x=1300, y=15)

if __name__=="__main__":
    b = 0
    w = Index_Principal()
    w.mainw.mainloop()