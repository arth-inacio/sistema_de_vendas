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
      
           

if __name__=="__main__":
    b = 0
    w = Index_Principal()