import PySimpleGUI as sg
from traducao import traduzir

class Tela_Python:
    def __init__(self):
        sg.change_look_and_feel("DarkBlue2")

        #Layout
        layout = [
            [sg.Text("Texto para traduzir:", size=(14,0)), sg.Input(size=(50,0), key="texto_p_traduzir")],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(64,10), text_color="white")]
        ]
        #Janela
        self.janela = sg.Window("Tradutor para Código Morse", element_justification="c").layout(layout)

    def Iniciar(self):
        while True:
            #Extrair Dados da Tela
            self.button, self.values = self.janela.Read()
            texto_para_traduzir = self.values["texto_p_traduzir"]
            traduzir(texto_para_traduzir)

tela = Tela_Python()
tela.Iniciar()