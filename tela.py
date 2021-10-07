import PySimpleGUI as sg

class Tela_Python:
    def __init__(self):
        sg.change_look_and_feel("DarkBrown4")

        #Layout
        layout = [
            [sg.Text("Nome:", size=(5,0)), sg.Input(size=(15,0), key="nome")],
            [sg.Text("Idade:", size=(5,0)), sg.Input(size=(15,0), key="idade")],
            [sg.Text("Quais provedores de email são aceitos?")],
            [sg.Checkbox("gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook"), sg.Checkbox("Yahoo", key="yahoo")],
            [sg.Text("Aceita cartão?")],
            [sg.Radio("sim", "Cartões", key="aceita_cartao"), sg.Radio("Não", "Cartões", key="nao_aceita_cartao")],
            [sg.Slider(range=(0,100), default_value=0, orientation="h", size=(15,20), key="sliderVelocidade")],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)

    def Iniciar(self):
        while True:
            #Extrair Dados da Tela
            self.button, self.values = self.janela.Read()
            nome = self.values["nome"]
            idade = self.values["idade"]
            aceita_gmail = self.values["gmail"]
            aceita_outlook = self.values["outlook"]
            aceita_yahoo = self.values["yahoo"]
            aceita_cartao = self.values["aceita_cartao"]
            nao_aceita_cartao = self.values["nao_aceita_cartao"]
            velocidade_script = self.values["sliderVelocidade"]
            print(f"nome: {nome}")
            print(f"idade: {idade}")
            print(f"aceita gmail: {aceita_gmail}")
            print(f"aceita outlook: {aceita_outlook}")
            print(f"aceita yahoo: {aceita_yahoo}")
            print(f"aceita cartão: {aceita_cartao}")
            print(f"não aceita cartão: {nao_aceita_cartao}")
            print(f"Velocidade Scripts: {velocidade_script}")

tela = Tela_Python()
tela.Iniciar()