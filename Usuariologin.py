from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self) -> None:
        self.loginwindow = Tk()
        self.loginwindow.title("Login")
        width = 1000
        height = 680
        self.loginwindow.iconbitmap(r'C:\\Users\\Arthur\\Documents\\GitHub\\sistema_de_vendas\\images\\icon.ico')
        tela_largura = self.loginwindow.winfo_screenwidth()
        tela_altura = self.loginwindow.winfo_screenheight()
        x = (tela_largura / 2) - (width / 2)
        y = (tela_altura / 2) - (height / 2)
        self.loginwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginwindow.resizable(0, 0)
        self.loginwindow.protocol("WM_DELETE_WINDOW", self.__login_del_)
        self.loginwindow.config(bg="#4267b2")

        self.username = StringVar(value="Nome Usuário")
        self.password = StringVar(value="Senha Usuário")
    
        self.obj_login()
    
    def __login_del_(self) -> None:
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.loginwindow.destroy()
            exit(0)

    def obj_login(self) -> None:
        self.loginframe = LabelFrame(self.loginwindow, width=600, height=300, bg="#4267b2", bd=0)
        self.loginframe.place(x=200, y=200)

        self.toplabel = Label(self.loginframe, fg="white", bg="#4267b2", anchor="center", text="Login", font="roboto 20 bold underline")
        self.toplabel.place(x=150, y=20)

        self.us = ttk.Entry(self.loginframe, textvariable=self.username, width=30, font="roboto 12")
        self.us.place(x=150, y=80, height=40)

        self.pa = ttk.Entry(self.loginframe, textvariable=self.password, width=30, show="*", font="roboto 12")
        self.pa.place(x=150, y=120, height=40)

        self.us.bind("<Button-1>", self.onclick_usuario)
        self.pa.bind("<Button-1>", self.onclick_senha)

        self.signin = Button(self.loginframe, text="Entrar", width=20, height=1, bg="darkgreen", fg="white", command=self.sucesso_login, font="roboto 12 bold", bd=0)
        self.signin.place(x=150, y=180)
    
    def verifica_erros(self) -> None:
        messagebox.showerror("Erro", "Nome de Usuário ou Senha Incorreta")
      
    def sucesso_login(self) -> None:
        messagebox.showinfo("Login", "Login efetuado com sucesso")
        self.loginwindow.quit()

    def onclick_usuario(self) -> None:
        self.us.delete(0, "end")
    
    def onclick_senha(self) -> None:
        self.pa.delete(0, "end")
        self.pa.config(show="*")
