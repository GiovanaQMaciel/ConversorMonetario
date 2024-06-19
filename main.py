#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que fará a janela
import customtkinter
from cotacoes_pegar_moedas import nomes_moedas, conversoes_disponiveis
from receber_cotacao import pegar_cotacao_moeda

#criar e configurar a janela
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("475x620")
janela.title("Conversor de Moedas")
janela.iconbitmap("dolar.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#Criar as botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor Monetário", text_color="#57DCDE", font=("",40))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("",18),) 
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("",18)) 

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis [moeda_selecionada]
    campo_destino.configure(values=lista_moedas_destino)
    campo_destino.set(lista_moedas_destino[0])

campo_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()) , command=carregar_moedas_destino ,font=("",14), fg_color= "orange", width=160, height=35)
campo_destino = customtkinter.CTkOptionMenu(janela, values= ["Selecione uma moeda de origem"], font=("",14), fg_color= "orange", width=160, height=35)
espaco = customtkinter.CTkLabel(janela, text="")

def converter_moeda():
    moeda_origem = campo_origem.get()
    moeda_destino = campo_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda (moeda_origem ,moeda_destino)
    texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("",16), width=200, height=40, hover=True)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="" ,font=("",16))

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    text_moeda = customtkinter.CTkLabel(lista_moedas, text= f"{codigo_moeda}: {nome_moeda}")
    text_moeda.pack()



#colocar os elementos criados na tela
titulo.pack(padx=10, pady=30)
texto_moeda_origem.pack(padx=10, pady=2)
campo_origem.pack(padx=10, pady=2)
espaco.pack(padx=10, pady=5)
texto_moeda_destino.pack(padx=10, pady=2)
campo_destino.pack(padx=10, pady=2)
botao_converter.pack(padx=10, pady=40)
texto_cotacao_moeda.pack(padx = 10, pady=10)
lista_moedas.pack(padx=10, pady=10)


#rodar a janela
janela.mainloop()



