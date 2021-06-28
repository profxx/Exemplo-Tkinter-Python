"""
Aula 34
- Iniciar um novo app (revisando)
- Colocar comando em um botão
- Alternar Janelas (quando você entra em uma nova janela)
- Tirar dúvidas (parte mais importante)
"Só tem dúvida quem estuda."
"""
from tkinter import *

class Anuncios(Toplevel):
    def __init__(self, original):
        self.frame_original = original
        
        Toplevel.__init__(self) # Importanto Método construtor
        self.geometry('375x667+979+15')
        self.title('ANÚNCIOS - SEJA BEM-VINDO(A)')
        self.configure(bg='#123456')

        self.btn = Button(
            self, 
            text='VOLTAR', 
            command=self.onClose)
        self.btn.pack()

    def onClose(self):
        self.destroy()
        self.frame_original.show()    


class App:
    # Cores
    cor_amarela ='#F5C983'
    cor_preta ='#140B0C'
    cor_branca ='#FFFFFF'
    cor_marrom ='#593435'
    cor_pele ='#E2B9B0'

    def __init__(self): # Método construtor
        self.root = root 
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()
    def tela(self):
        self.root.title('App de Moda') # Título
        self.root.geometry('375x667+979+15') # Geometria
        self.root.iconbitmap('mmara.ico') # Ícone
        self.root.configure(bg = self.cor_amarela)
        # self.root.state('zoomed') # Começar maximizado
    def frames(self):
        self.frame1 = Frame(self.root, bg=self.cor_branca)
        self.frame1.place(
            relx=0.05, 
            rely=0.025, 
            relwidth=0.90,
            relheight=0.80)
        
        self.frame2 = Frame(self.root, bg=self.cor_marrom)
        self.frame2.place(
            relx=0.05,
            rely=0.825,
            relwidth=0.90,
            relheight=0.175
        )
    def widgets_frame1(self):
        self.modelo = PhotoImage(file='moda.png')
        self.img1 = Label(
            self.frame1, 
            image=self.modelo,
            bd=0
            )
        self.img1.place(
            relx=0.30,
            rely=0.20,
        )
    def widgets_frame2(self):
        self.btn_entrar = Button(
            self.frame2, # Onde está localizado
            text='Entrar', # Texto do botão
            bg=self.cor_marrom, # Cor de fundo (background)
            activebackground=self.cor_marrom, # Cor clicado
            font=('helvetica', 20), # Fonte
            fg=self.cor_amarela, # Cor da fonte
            activeforeground=self.cor_amarela, # Cor fonte clicado
            command=self.clica_entrar
            )
        self.btn_entrar.place(
            relx=0,
            rely=0,
            relwidth=0.50,
            relheight=1.00
            )

        self.btn_perfil = Button(
            self.frame2,
            text='Perfil',
            bg=self.cor_marrom,
            activebackground=self.cor_marrom,
            fg=self.cor_amarela,
            activeforeground=self.cor_amarela,
            font=('helvetica', 20)
            )
        self.btn_perfil.place(
            relx=0.50, 
            rely=0, 
            relwidth=0.50, 
            relheight=1.00
            )
    # Entrar em outra janela
    # Precisamos CLICA_ENTRAR (comando btn), HIDE, SHOW
    def clica_entrar(self): # Comando btn
        self.hide()
        self.subFrame = Anuncios(self)
    def hide(self): # Esconde a root
        self.root.withdraw()
    def show(self): # Mostra a outra janela
        self.root.update()
        self.root.deiconify()




##### Programa Principal #####
root = Tk()
App()