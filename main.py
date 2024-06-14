#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que fará a janela
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("475x620")

#Criar as botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor Monetário", text_color="#58FCEC", font=("",40))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("",18),) 
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("",18)) 
campo_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"],font=("",14), fg_color= "orange", width=160, height=35)
campo_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], font=("",14), fg_color= "orange", width=160, height=35)
espaco = customtkinter.CTkLabel(janela, text="")

def converter_moeda():
    print("Moeda Convertida")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("",16), width=200, height=40, hover=True)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dolár Americano", "EUR: Euro", "BRL: Real Brasileiro", "BTC: Bitcoin"]

for moeda in moedas_disponiveis:
    text_moeda = customtkinter.CTkLabel(lista_moedas, text= moeda)
    text_moeda.pack()



#colocar os elementos criados na tela
titulo.pack(padx=10, pady=30)
texto_moeda_origem.pack(padx=10, pady=2)
campo_origem.pack(padx=10, pady=2)
espaco.pack(padx=10, pady=5)
texto_moeda_destino.pack(padx=10, pady=2)
campo_destino.pack(padx=10, pady=2)
botao_converter.pack(padx=10, pady=40)
lista_moedas.pack(padx=10, pady=10)


#rodar a janela
janela.mainloop()



