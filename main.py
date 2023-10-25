######################################################################
#     Se precisar de ajuda com o código abaixo, pode me chamar       #
#             no WhatsApp +55 (14) 99723-7199 (Ricardo Lima)         #
######################################################################

import customtkinter as ctk
from PIL import Image,ImageTk
import pyautogui as aut
import time
import os


janela = ctk.CTk()#iniciando o app
janela.geometry("760x450")#Tamanho do app
janela.resizable(False, False)#Congelando a tela do App
janela.title("ERP BOT v2.8")#titulo do app v2.8
ctk.set_appearance_mode("light")#tema padrão do app
janela.iconbitmap('icon.ico')#icone padrão do app


#Fontes utilizadas no App
Font_tuple = ("Microsoft YaHei UI Light", 12, "bold")
font_ver = ("Lucida Sans", 15, "bold")
font_autor = ("Eras Light ITC", 16, "italic")
Font_tuple1 = ("Microsoft YaHei UI Light", 14, "bold")
font_olho = ('Eras Light ITC',11,'bold')

def showH():#botão de ver senha
    caixaDeEntrada2.configure(show="")
    verocultarsenha.destroy()
def entrar():#função utilizada para dar informações 
    selectTemp.get()#seleciona o tempo de execução das tarefas
    usuario = caixaDeEntrada1.get()#pega o usuario
    senha = caixaDeEntrada2.get()#pega senha
    box1 = selectBox1.get()#pega a base seleciona
    box2 = selectBox2.get()#pega a base seleciona
    box3 = selectBox3.get()#pega a base seleciona
    box4 = selectBox4.get()#pega a base seleciona
    box5 = selectBox5.get()#pega a base seleciona
    box6 = selectBox6.get()#pega a base seleciona
    while True:# estrutura de repetição para funcionar o app 
        if box1 =="Selecione uma Base" and box2 =="Selecione uma Base" and box3 == "Selecione uma Base" and box4 =="Selecione uma Base" and box5 =="Selecione uma Base" and box6 =="Selecione uma Base":#condição para bases nao selecionadas
            aut.alert(text=" Insira ao menos 1 Base, para que o Robo inicie!", title="ERR0R", button="OK")
            break
        if senha == "" or usuario == "":# condição para usuario e senha
            aut.alert(text=' Você não inserio um usuario ou senha para começar!!', title='Insira novamente', button='Tentar novamente')
            break
        if senha =="": #condição para ver senha digitada
            caixaDeEntrada2.configure(show="*")
        else:
            pass
                # verocultarsenha.pack()
            verocultarsenha.configure(janela, text="Ver",font=font_olho)
        if box1 == "Selecione uma Base":
            pass
        else:

                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box1)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)


        if box2 == "Selecione uma Base":
            pass
        else:
                
                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box2)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)
        if box3 == "Selecione uma Base":
            pass
        else:
                
                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box3)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)
        if box4 == "Selecione uma Base":
            pass
        else:
                
                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box4)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)

        if box5 == "Selecione uma Base":
            pass
        else:
                
                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box5)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)
        if box6 == "Selecione uma Base":
            pass
        else:
                
                        #                                               Abrir o Corporate
            os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
            time.sleep(6)#                                         Inserindo o usuario
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.press('Tab')
            aut.write(usuario)
            time.sleep(1)
                                #                                               colocar a senha
            aut.press('Tab')
            aut.write (senha)
                                #                                               mudar a matriz desejada
            aut.press('Tab')
            aut.write(box6)
            time.sleep(1)
            aut.press('Enter')
                                #                                               entrar
            aut.press('Enter')
            time.sleep(selectTemp)
        break   

#Imagem da logo Corporate
img = (Image.open("logo.png"))
resized_image= img.resize((180,180))
my_img=ImageTk.PhotoImage(resized_image)

#colocando a imagem em Label e customizando Logo Corporate
label= ctk.CTkLabel(janela, image=my_img,text="")
label.pack()
label.place(x=50, y=20)

#Imagem do Corporate
img = (Image.open("corporate.png"))
resized_image= img.resize((350,100))
my_img=ImageTk.PhotoImage(resized_image)

#colocando a imagem em Label e customizando Corporate Text
label= ctk.CTkLabel(janela, image=my_img,text="")
label.pack()
label.place(x=350, y=25)

#colocando o usuario em Label e customizando Usuario Text
text1 = ctk.CTkLabel(master=janela,text="Usuário:")
text1.pack()
text1.place(x=360,y=150)
text1.configure(Font_tuple)
caixaDeEntrada1 = ctk.CTkEntry(janela,width=335)
caixaDeEntrada1.place(x=360, y=180)
caixaDeEntrada1.configure(Font_tuple)

#colocando o senha em Label e customizando Senha Text
text2 = ctk.CTkLabel(master=janela,text="Senha:")
text2.pack()
text2.place(x=360,y=230)
text2.configure(font= Font_tuple)

#botão para ver senha
verocultarsenha = ctk.CTkButton(master=janela,
                                text="MOSTRAR",
                                command=showH,
                                height=(10),
                                width=(90))
verocultarsenha.place(x=603,y=235)

caixaDeEntrada2 = ctk.CTkEntry(janela,width=335, show='*')
caixaDeEntrada2.place(x=360, y=260)
caixaDeEntrada2.configure(font= Font_tuple)


#botão para acionar função ENTRAR
buttonVer = ctk.CTkButton(master=janela,
                        text="Entrar",
                        command=entrar,
                        height=(30),
                        width=(172))
buttonVer.pack(padx=5, pady=10)
buttonVer.place(x=360,y=390)
buttonVer.configure(font= Font_tuple1)


#caixa de seleção das bases
selectText1 = ctk.CTkLabel(master=janela,text="BASE 1")
selectText1.pack()
selectText1.place(x=5,y=200)
selectText1.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox1 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox1.pack()
selectBox1.set('Selecione uma Base')
selectBox1.place(x=60,y=200)


#caixa de seleção das bases
selectText1 = ctk.CTkLabel(master=janela,text="BASE 2")
selectText1.pack()
selectBox1.set('Selecione uma Base')
selectText1.place(x=5,y=240)
selectText1.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox2 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox2.set('Selecione uma Base')
selectBox2.pack()
selectBox2.place(x=60,y=240)


#caixa de seleção das bases
selectText1 = ctk.CTkLabel(master=janela,text="BASE 3")
selectText1.pack()
selectText1.place(x=5,y=280)
selectText1.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox3 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox3.set('Selecione uma Base')
selectBox3.pack()
selectBox3.place(x=60,y=280)


#caixa de seleção das bases
selectText4 = ctk.CTkLabel(master=janela,text="BASE 4")
selectText4.pack()
selectText4.place(x=5,y=320)
selectText4.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox4 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox4.pack()
selectBox4.set('Selecione uma Base')
selectBox4.place(x=60,y=320)


#caixa de seleção das bases
selectText5 = ctk.CTkLabel(master=janela,text="BASE 5")
selectText5.pack()
selectText5.place(x=5,y=360)
selectText5.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox5 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox5.pack()
selectBox5.set('Selecione uma Base')
selectBox5.place(x=60,y=360)


#caixa de seleção das bases
selectText6 = ctk.CTkLabel(master=janela,text="BASE 6")
selectText6.pack()
selectText6.place(x=5,y=400)
selectText6.configure(font= Font_tuple)
bases = ['Selecione uma Base','LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]  
selectBox6 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox6.pack()
selectBox6.set('Selecione uma Base')
selectBox6.place(x=60,y=400)


#caixa de entrada de tempo a ser utilizado
label4 = ctk.CTkLabel(janela,text="Selecione o tempo de execução desejado:")
label4.pack()
label4.place(x=360,y=300)
label4.configure(font=Font_tuple)

times = ['5','8','10','15','20','25']
selectTemp = ctk.CTkOptionMenu(janela,values=times,width=335)
selectTemp.set(5)
selectTemp.pack()
selectTemp.place(x=360, y=330)
selectTemp.configure()

# EM CASO DE UTILIZAÇÃO DO APP, NUNCA RETIRAR ASSINATURA DO AUTOR! Obrigado.
label3 = ctk.CTkLabel(janela,text="@AUTOR: Ricardo Rodrigues Lima")
label3.pack()
label3.place(x=260,y=425)
label3.configure(font=font_autor)


# EM CASO DE UTILIZAÇÃO DO APP, NUNCA RETIRAR ASSINATURA DO AUTOR! Obrigado.

janela.mainloop()

######################################################################
#     Se precisar de ajuda com o código abaixo, pode me chamar       #
#             no WhatsApp +55 (14) 99723-7199 (Ricardo)              #
######################################################################