#sempre que você estiver travado 
#Escrever o passo a passo da automação

import pyautogui
import time



#pyautogui.click -> clicar com o mouse
#pyautogui.write - > escrever um texto 
#pyautogui.press -> apertar 1 tecla
#pyautogui.hotkey -> atalho#

pyautogui.PAUSE = 0.3

#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#2 - fazer login no sistema da empresa
pyautogui.click(x=747, y=393)
pyautogui.write("victortreinos@gmail.com")

pyautogui.press("tab")
pyautogui.write('123456')
pyautogui.press("enter")


time.sleep(3)

#3 - importar a base de dados dos produtos
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #INDEX no python são linhas, por isto é .INDEX
    #4 - cadastrar 1 produto
    pyautogui.click(x=808, y=277)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]


    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #apertar botao enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000) #núemros positivos CIMA, numeros negativos PARA BAIXO



#5 - repetir o cadastro para todos os produtos

