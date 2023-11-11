import sqlite3
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class Login:
    def __init__(self) -> None:
        self.loginwindow = Tk()
        self.loginwindow.title("Login: ")
        width = 1000
        height = 680
        self.loginwindow.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\favicon.ico')
        self.loginwindow.config(bg="darkgreen")

        tela_largura = self.loginwindow.winfo_screenwidth()
        tela_altura = self.loginwindow.winfo_screenheight()
        x = (tela_largura / 2) - (width / 2)
        y = (tela_altura / 2) - (height / 2)
        self.loginwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginwindow.resizable(0, 0)
        self.obj_login()
    
    def obj_login(self):
        self.loginframe = LabelFrame(self.loginwindow, width=600, height=300, bg="lightblue", bd=0)
        self.loginframe.place(x=200, y=200)

        self.toplabel = Label(self.loginframe, fg="black", bg="lightblue", anchor="center", text="Login", font="roboto 20 bold underline")
        self.toplabel.place(x=150, y=20)

        self.us = ttk.Entry(self.loginframe, width=30, font="roboto 12")
        self.us.place(x=150, y=80, height=40)

        self.pa = ttk.Entry(self.loginframe, width=30, show="*", font="roboto 12")
        self.pa.place(x=150, y=120, height=40)
