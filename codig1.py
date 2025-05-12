import pandas as ps
import pyautogui
import time
# abrir o sistema

pyautogui.PAUSE = 1
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
pyautogui.click(x=884, y=645)
time.sleep(3)
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=940, y=376)


# #sistema: https://dlp.hashtagtreinamento https://dlp.hashtagtreinamentos.com/python/intensivao/login
#  https://dlp.hashtagtreinamentos.com/python/intensivao/login
# s.com/python/intensivao/login 
# fazer o loguim

pyautogui.write("henriquerh2320077@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")

# importar a base de dados dos produtos
tabela = ps.read_csv("produtos.csv")
print(tabela)

#CADASTRAR um produto MOLO000251    
#codigo,#marca,#tipo,#categoria,#preco_unitario#custo,#obs
time.sleep(3)

# repetir o passo até acabar todos os produtos
for linha in tabela.index:
    pyautogui.click(x=841, y=256)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not ps.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")    

    