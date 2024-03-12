import pyautogui # PACOTE PARA AUTOMAÇÃO
import time
import pandas # PACOTE PARA IMPORTAÇÃIO DE BASE DE DADOS

# ABRIR NAVEGADOR E SITE PARA FAZER LOGIN
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# IMPORTAR BASE DE DADOS
# CADASTRAR 1 PRODUTO
# REPETIR PROCESSO DE CADASTRO ATÉ FINALIZAR

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


pyautogui.PAUSE = 0.8
#  PASSO 1 = ABRIR NAVEGADOR (Edge)
pyautogui.press("win")
pyautogui.write(" Edge")
pyautogui.press("enter")
pyautogui.click(x=468, y=51)

# PASSO 2 = ABRIR LINK DE LOGIN
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #tempo de espera para a pagina web carregar

# PASSO 2.1 = FAZER LOGIN
pyautogui.click(x=829, y=359)
pyautogui.write("emailaleatorio@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaaleatoria")
pyautogui.press("enter")

# PASSO 2.2 = LEITURA DA TABELA

tabela = pandas.read_csv("produtos_tabela_para_teste.csv") 
print (tabela)

# PASSO 3 = CADASTRAR PRODUTO
for linha in tabela.index:  
    pyautogui.click(x=708, y=241) #variavel para clicar no 1º campo
    codigo = tabela.loc[linha, "codigo"] #variavel para verificar a localização da informação na tabela, e pegar para preencher no campo

    # PASSO 3.1 = PREENCHER CAMPO
    pyautogui.write(str(codigo))
    # PASSO 3.2 = PASSAR PARA O PROXIMO CAMPO
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pandas.isna(tabela.loc[linha, "obs"]):  # verificar se existe informação em (obs), caso contrario, não preencher.
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastrar produto -> botão enviar
    pyautogui.scroll(5000) # comando para dar scroll na tela ate o inicio caso seja necessario.




