from tkinter import *

class Admin:
    def __init__(self, mainw) -> None:
        self.mainw=mainw

    def admin_mainmenu(self, a, b) -> None:
        self.mainw.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')
        self.mainframe = LabelFrame(self.mainw, width=850, height=95, bg="#f7f7f7")
        self.mainframe.place(x=50, y=100)

        mi = PhotoImage(file="images/carrinho.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="ITEMS", bd=0, font="roboto 11 bold", image=mi)
        self.aitems.image = mi
        self.aitems.place(x=260, y=17)

        mi = PhotoImage(file="images/nota.png")
        mi = mi.subsample(a,b)
        self.aitems = Button(self.mainframe, text="NOTAS",bd=0,font="roboto 11 bold", image=mi)
        self.aitems.image = mi
        self.aitems.place(x=62, y=17)

        mi = PhotoImage(file="images/usertrocar.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="SAIR",bd=0,font="roboto 11 bold", image=mi)
        self.changeuser.image = mi
        self.changeuser.place(x=460, y=17)

        mi = PhotoImage(file="images/sair.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="FECHAR",bd=0,font="roboto 11 bold", image=mi)
        self.logout.image = mi
        self.logout.place(x=670, y=17)

        mi = PhotoImage(file="images/perfil1.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="PERFIL1",bd=0,font="roboto 11 bold", image=mi)
        self.logout.image = mi
        self.logout.place(x=800, y=17)

        self.tableframe1 =Frame(self.mainw, width=150, height=400,bg="#9ACD32")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe1info=self.tableframe1.place_info()

        self.tableframe =Frame(self.mainw, width=350, height=700,bg="#9ACD32")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()

        self.itemframe = Frame(self.mainw, width=800, height=350, bg="#9ACD32")
        self.itemframe.place(x=810, y=460+20)
        self.itemframeinfo = self.itemframe.place_info()

        self.searchframe = Frame(self.mainw, width=800, height=350, bg="#9ACD32")
        self.searchframe.place(x=575, y=260)
        self.searchframeinfo=self.searchframe.place_info()

        self.searchbut = Button(self.searchframe, text="Pesquisar Descricao", font="roboto 14 bold", bd=1, bg="#9ACD32")
        self.searchbut.place(x=0, y=20, height=40)

        self.resetbut = Button(self.searchframe, text="Restabelecer", font="roboto 14 bold", bd=1, width=10, bg="#9ACD32")
        self.resetbut.place(x=0, y=60, height=40)

        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#9ACD32")
        self.entryframe1.place(x=230, y=470+20)
        self.entryframe1info=self.entryframe1.place_info()
