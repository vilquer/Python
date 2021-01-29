from tkinter import *
import consulta
import config


def botao(x,y):
    consulta.consulta(tipo_consulta='cnpj', objeto_consulta=x, qualificacoes=config.QUALIFICACOES,  path_BD=config.PATH_BD, nivel_max=y, 
                path_output='folder', csv=False , colunas_csv=config.COLUNAS_CSV, 
                csv_sep=config.SEP_CSV, graphml=False, gexf=False, viz=True, path_conexoes=None  )

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Pesquisa Gráfico de Relacionamento")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cnpjLabel = Label(self.segundoContainer,text="CNPJ", font=self.fontePadrao)
        self.cnpjLabel.pack(side=LEFT)

        self.cnpj = Entry(self.segundoContainer)
        self.cnpj["width"] = 30
        self.cnpj["font"] = self.fontePadrao
        #self.cnpj.insert(0, "00000000000191")
        self.cnpj.pack(side=LEFT)

        self.nivelLabel = Label(self.terceiroContainer, text="Nível  ", font=self.fontePadrao)
        self.nivelLabel.pack(side=LEFT)

        self.nivel = Entry(self.terceiroContainer)
        self.nivel["width"] = 30
        self.nivel["font"] = self.fontePadrao
        #self.nivel["show"] = "*"
        self.nivel.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Pesquisar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificanivel
        self.autenticar.pack()



    #Método verificar nivel
    def verificanivel(self):
        cnpj = self.cnpj.get()
        nivel = self.nivel.get()
        botao(cnpj,int(nivel))
            




root = Tk()
root.title('Pesquisa Dados RFB - base 04/20')
Application(root)
root.mainloop()