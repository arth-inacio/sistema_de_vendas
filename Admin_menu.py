import sqlite3
from tkinter import ttk
from tkinter import *


class Admin:
    def admin_mainmenu(self, a, b):
        self.mainframe = LabelFrame(self.mainwindow, width=1200, height=145, bg="#f7f7f7", bd=0)
        self.mainframe.place(x=100, y=100)

        self.conta = Button(self.mainframe, text="Perfil", bd=1, font="roboto 11 bold", compound=TOP)
        self.conta.place(x=655, y=27)

        self.sair = Button(self.mainframe, text="Sair", bd=1, font="roboto 11 bold", compound=TOP)
        self.sair.place(x=1050, y=27)

        self.trocarusuario = Button(self.mainframe, text="Trocar Usuário", bd=1, font="roboto 11 bold", compound=TOP)
        self.trocarusuario.place(x=855, y=27)

        self.items = Button(self.mainframe, text="Itens", bd=1, font="roboto 11 bold", compound=TOP)
        self.items.place(x=47, y=27)

        self.Estoque = Button(self.mainframe, text="Inventario", bd=1, font="roboto 11 bold", compound=TOP)
        self.Estoque.place(x=255, y=27)

        self.vendas = Button(self.mainframe, text="Vendas", bd=1, font="roboto 11 bold", compound=TOP)
        self.vendas.place(x=455, y=27)

        self.formframe = Frame(self.mainwindow, width=500, height=550, bg="yellow")
        self.formframe.place(x=100, y=315)