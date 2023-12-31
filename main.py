import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from User_menu import User
from Intro import Splash


class Main(Splash, Login, User):
    def __init__(self) -> None:
        global b
        if b==0:
            super().__init__()
            b=1
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  
        self.mainw = Toplevel(bg="#FFFFFF")
        width = 1386
        height = 780
        self.loginw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("Tobacco Realm")
        self.mainw.resizable(0,0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

    def __Main_del__(self) -> None:
        if messagebox.askyesno("Sair", "Deseja realmente sair do sistema?") == True:
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

    def getdetails(self) -> None:
        self.buildmain()
 
    def buildmain(self) -> None:
        if self.account_type == 'ADMIN':
            pass

        super(User).__init__()
        self.user_mainmenu(8,8)
        self.loginw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')
        self.logout.config(command=self.__Main_del__)
        self.changeuser.config()
        self.topframe=LabelFrame(self.mainw, width=1800, height=120, bg="#8A2BE2")
        self.topframe.place(x=0, y=0)
        
        self.storelable=Label(self.topframe, text="Tobacco Realm", bg="darkgreen", justify="center")
        self.storelable.config(font="Roboto 30 bold", fg="snow")
        self.storelable.place(x=360, y=30)

        mi = PhotoImage(file="images/perfil1.png")
        mi = mi.subsample(4,4)
        self.myprofile = ttk.Label(self.topframe, text=(self.username.get()).capitalize(), image=mi)
        self.myprofile.image = mi
        self.myprofile.place(x=1300, y=15)
            
if __name__ == '__main__':
    b=0
    w = Main()
    w.base.commit()
    w.mainw.mainloop()
