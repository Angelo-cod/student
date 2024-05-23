from tkinter import *
from tkinter import ttk

#Cores para usar no app
cor_preto = "#000000"
cor_azul = "#0000FF"
cor_cinza = "#363636"
cor_cian = "#20B2AA"
cor_verde = "#3CB371"
cor_vermelho = "#FF0000"
cor_amarelo = "#FFFF00"
cor_branco = "#FFFFFF"
cor = cor_azul

janela = Tk() 
janela.title("Jogo da velha")
janela.geometry('260x380')
janela.configure(bg=cor_preto)

primeiro_frame = Frame(janela, width=240, height=100, bg=cor_cinza, relief="raised")
primeiro_frame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

segundo_frame = Frame(janela, width=240, height=240, bg=cor_cinza, relief="flat")
segundo_frame.grid(row=1, column=0, sticky=NW, padx=10, pady=10)

player_x = Label(primeiro_frame, text="X", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 40 bold'), fg=cor_azul )
player_x.place(x=25, y=10)
player_x_name = Label(primeiro_frame, text="Jogador 1", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 8 bold'), fg=cor_branco )
player_x_name.place(x=17, y=70)

placar_x = Label(primeiro_frame, text= "0", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 25 bold'), fg=cor_branco )
placar_x.place(x=80, y=21)

separador = Label(primeiro_frame, text=":", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 27 bold'), fg=cor_branco)
separador.place(x=110, y=18)

player_o = Label(primeiro_frame, text="0", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 40 bold'), fg=cor_vermelho)
player_o.place(x=175, y=10)
player_o_name = Label(primeiro_frame, text="Jogador 2", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 8 bold'), fg=cor_branco )
player_o_name.place(x=167, y=70)

placar_o = Label(primeiro_frame, text= "0", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 25 bold'), fg=cor_branco )
placar_o.place(x=135, y=21)

jogando = "X"
quem_joga = ""
rodada = 0
count = 0
score_x = 0
score_o = 0
campeao = "X"

table = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
fim_jogo_x = ""
fim_jogo_o = ""



def inicio():
    b_iniciar.place(x=500, y=500)
    global score_x
    global score_o
    placar_x['text'] = '0'
    placar_o['text'] = '0'
    score_x = 0
    score_o = 0
    partida.place(x=500, y=500)
    nomes.place(x=400, y=500)
    
    
    

    table[0][0] = ""
    table[0][1] = ""
    table[0][2] = ""
    table[1][0] = ""
    table[1][1] = ""
    table[1][2] = ""
    table[2][0] = ""
    table[2][1] = ""
    table[2][2] = ""
    
    def controlar(i):
        global jogando
        global quem_joga
        global count
        global cor
        partida.destroy
        
        
        
        
        if i==str(1):
        
            if botao_1['text'] == "":
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_1['fg'] = cor
                botao_1['text'] = jogando
                table[0][0] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
               
                
        if i==str(2):
            if botao_2['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_2['fg'] = cor
                botao_2['text'] = jogando
                table[0][1] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
                
                       
        if i==str(3):
            if botao_3['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_3['fg'] = cor
                botao_3['text'] = jogando
                table[0][2] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
            
                                     
        if i==str(4):
            if botao_4['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_4['fg'] = cor
                botao_4['text'] = jogando
                table[1][0] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
                
      
        if i==str(5):
            if botao_5['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_5['fg'] = cor
                botao_5['text'] = jogando
                table[1][1] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
               
                
        if i==str(6):
            if botao_6['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_6['fg'] = cor
                botao_6['text'] = jogando
                table[1][2] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
                
                        
        if i==str(7):
            if botao_7['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_7['fg'] = cor
                botao_7['text'] = jogando
                table[2][0] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
              
                
        if i==str(8):
            if botao_8['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_8['fg'] = cor
                botao_8['text'] = jogando
                table[2][1] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
                print(count)
               
                                  
        if i==str(9):
            if botao_9['text'] == '':
                if jogando == "X":
                    cor = cor_azul
                if jogando == "O":
                    cor = cor_vermelho
                botao_9['fg'] = cor
                botao_9['text'] = jogando
                table[2][2] = jogando
                if jogando == "X":
                    jogando = "O"
                    quem_joga = "Jogador 1"
                else:
                    jogando = "X"
                    quem_joga = "Jogador 2"

                count += 1
            
                
                print(count)
                

        if count >= 5:
            if table[0][0] == table[0][1] == table[0][2] != "":
                vencedor(jogando)
            elif table[1][0] == table[1][1] == table[1][2] != "":
                vencedor(jogando)
            elif table[2][0] == table[2][1] == table[2][2] != "":
                vencedor(jogando)
                    
            if table[0][0] == table[1][0] == table[2][0] != "":
                vencedor(jogando)
            elif table[0][1] == table[1][1] == table[2][1] != "":
                vencedor(jogando)
            elif table[0][2] == table[1][2] == table[2][2] != "":
                vencedor(jogando)

            if table[0][0] == table[1][1] == table[2][2] != "":
                vencedor(jogando)
            elif table[2][0] == table[1][1] == table[0][2] != "":
                vencedor(jogando)


            if count >= 9:
                vencedor("Foi empate")
           
        
    def vencedor(i):
        global rodada 
        global count
        global score_x
        global score_o
        global table

        botao_1['state']='disable'
        botao_2['state']='disable'
        botao_3['state']='disable'
        botao_4['state']='disable'
        botao_5['state']='disable'
        botao_6['state']='disable'
        botao_7['state']='disable'
        botao_8['state']='disable'
        botao_9['state']='disable'

        count = 0

        venceu = Label(segundo_frame, text="", height=1, width=22, relief=RAISED, font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_branco )
        venceu.place(x=40,y=150)

        # linhas_vertiais1.place(x=500, y=1500)
        # linhas_vertiais2.place(x=500, y=1500)
        # linhas_horizontais1.place(x=500, y=1500)
        # linhas_horizontais2.place(x=500, y=1500)

        # b_reiniciar.place(x=90,y=198)

        if i == "X":
            score_o += 1
            venceu['text'] = "Jogador 2 venceu a rodada"
            placar_o['text'] = score_o
            
        if i == "O":
            score_x += 1
            venceu['text'] = "Jogador 1 venceu a rodada"
            placar_x['text'] = score_x

        if i == "Foi empate":
            venceu['text'] = "Foi empate!"
        
        # if score_x == 3:
        #     venceu['text'] = "Jogador 1 venceu a partida!"
        #     denovo = Button(segundo_frame, command=inicio ,text="iniciar outra rodada", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
        #     denovo.place(x=90,y=198)
           
            
        # if score_o == 3:
        #     venceu['text'] = "Jogador 2 venceu a partida"
        #     denovo = Button(segundo_frame, command=inicio ,text="iniciar outra rodada", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
        #     denovo.place(x=90,y=198)
            


        # botao_1['text']=''
        # botao_2['text']=''
        # botao_3['text']=''
        # botao_4['text']=''
        # botao_5['text']=''
        # botao_6['text']=''
        # botao_7['text']=''
        # botao_8['text']=''
        # botao_9['text']=''

        def reiniciar():
            denovo.destroy()
            
           
            botao_1['text']=""
            botao_2['text']=""
            botao_3['text']=""
            botao_4['text']=""
            botao_5['text']=""
            botao_6['text']=""
            botao_7['text']=""
            botao_8['text']=""
            botao_9['text']=""

            botao_1['state']="normal"
            botao_2['state']="normal"
            botao_3['state']="normal"
            botao_4['state']="normal"
            botao_5['state']="normal"
            botao_6['state']="normal"
            botao_7['state']="normal"
            botao_8['state']='normal'
            botao_9['state']='normal'

            table[0][0] = ""
            table[0][1] = ""
            table[0][2] = ""
            table[1][0] = ""
            table[1][1] = ""
            table[1][2] = ""
            table[2][0] = ""
            table[2][1] = ""
            table[2][2] = ""

            

            venceu.destroy()
            b_reiniciar.destroy()
            denovo.destroy()

       
        if score_x < 3 and score_o < 3:
            denovo = Button(segundo_frame, command=reiniciar ,text="iniciar outra rodada", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
            denovo.place(x=90,y=198)
            

        if score_o == 3 or score_x == 3:

            if score_x == 3:
                venceu['text'] = "Jogador 1 venceu a partida!"
                partida.place(x=90,y=198)
           
            
            if score_o == 3:
                venceu['text'] = "Jogador 2 venceu a partida"
                partida.place(x=90,y=198)
                

            
        

            

        
        
        def end_game():
            global table
            global count
            global rodada
            global placar_x
            global placar_o
            placar_x = Label(primeiro_frame, text= "0", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 25 bold'), fg=cor_branco )
            placar_o = Label(primeiro_frame, text= "0", height=1, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 25 bold'), fg=cor_branco )

            #venceu.destroy()
            #b_reiniciar.destroy()

            if rodada >= 5:
                end_game()
            else:
                rodada += 1
                table = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
                count = 0

            fim()

            # if rodada >= 5:
            #     end_game()
            # else:
            #     rodada += 1
            #     table = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
            #     count = 0
        
            
    def fim():
        global rodada 
        global count
        global score_x
        global score_o
        global table

        rodada  = 0
        count   = 0
        score_x = 0
        score_o = 0
        table = [["1","2","3"], ["4","5","6"], ["7","8","9"]]


        botao_1['text']=""
        botao_2['text']=""
        botao_3['text']=""
        botao_4['text']=""
        botao_5['text']=""
        botao_6['text']=""
        botao_7['text']=""
        botao_8['text']=""
        botao_9['text']=""

        table[0][0] = ""
        table[0][1] = ""
        table[0][2] = ""
        table[1][0] = ""
        table[1][1] = ""
        table[1][2] = ""
        table[2][0] = ""
        table[2][1] = ""
        table[2][2] = ""

        # botao_1['state']='disable'
        # botao_2['state']='disable'
        # botao_3['state']='disable'
        # botao_4['state']='disable'
        # botao_5['state']='disable'
        # botao_6['state']='disable'
        # botao_7['state']='disable'
        # botao_8['state']='disable'
        # botao_9['state']='disable'


        final = Label(segundo_frame, text="Fim de jogo", height=1, width=22, relief=RAISED, font=('Ivy 8 bold'), bg=cor_cinza, fg=cor_branco )
        final.place(x=90,y=100)

        def jogar_novamente():
            global count
            placar_x['text'] = 0
            placar_o['text'] = 0
            final.destroy()
            b_iniciar.destroy()
            count = 0

            table[0][0] = ""
            table[0][1] = ""
            table[0][2] = ""
            table[1][0] = ""
            table[1][1] = ""
            table[1][2] = ""
            table[2][0] = ""
            table[2][1] = ""
            table[2][2] = ""

           
            inicio()
        

        denovo = Button(segundo_frame, command=jogar_novamente ,text="iniciar outra rodada", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
        denovo.place(x=90,y=198)

    linhas_verticais1 = Label(segundo_frame, text="", height=23, relief=FLAT, pady=2, padx=2, anchor='center', font=('Ivy 5 bold'), bg=cor_branco)
    linhas_verticais1.place(x=90, y=15)
    linhas_verticais2 = Label(segundo_frame, text="", height=23, relief=FLAT, pady=2, padx=2, anchor='center', font=('Ivy 5 bold'), bg=cor_branco)
    linhas_verticais2.place(x=157, y=15)

    linhas_horizontais1 = Label(segundo_frame, text="", width=190, relief=FLAT, anchor='center', font=('Ivy 1 '), bg=cor_branco)
    linhas_horizontais1.place(x=30, y=63)
    linhas_horizontais2 = Label(segundo_frame, text="", width=190, relief=FLAT, anchor='center', font=('Ivy 1 '), bg=cor_branco)
    linhas_horizontais2.place(x=30, y=123)


    botao_1 = Button(segundo_frame ,command=lambda:controlar('1'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)  
    botao_1.place(x=33, y=9)
    botao_2 = Button(segundo_frame,command=lambda:controlar('2'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_2.place(x=101, y=9)
    botao_3 = Button(segundo_frame,command=lambda:controlar('3'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_3.place(x=167, y=9)

    botao_4 = Button(segundo_frame,command=lambda:controlar('4'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_4.place(x=33, y=72)
    botao_5 = Button(segundo_frame,command=lambda:controlar('5'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_5.place(x=101, y=72)
    botao_6 = Button(segundo_frame,command=lambda:controlar('6'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_6.place(x=167, y=72)

    botao_7 = Button(segundo_frame,command=lambda:controlar('7'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_7.place(x=33, y=132)
    botao_8 = Button(segundo_frame,command=lambda:controlar('8'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_8.place(x=101, y=132)
    botao_9 = Button(segundo_frame,command=lambda:controlar('9'), text="", width=3, font=('Ivy 18 bold'), overrelief=RIDGE, relief=FLAT, bg=cor_cinza)
    botao_9.place(x=167, y=132)

def creditos():
    b_creditos.place(x=500, y=500)
    b_iniciar.place(x=10, y=200)
    nomes = Label(segundo_frame, text="O jogo é humilde,\n porém, feito com muito\n esforço por:\n \n Bruno França\n Mariana Silva\n Priscilla\n Angelo Gabriel", height=8, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 12 bold'), fg=cor_cian )
    nomes.place(x=35, y=30)


b_iniciar = Button(segundo_frame, command=inicio ,text="iniciar", height=2, width=6, bg=cor_cinza, fg=cor_amarelo)
b_iniciar.place(x=90,y=100)
b_creditos = Button(segundo_frame,command=creditos, text="Créditos", width=6, bg=cor_cinza, fg=cor_cian, relief=RAISED)
b_creditos.place(x=10, y=213)
b_reiniciar = Button(segundo_frame, command=inicio ,text="iniciar outra rodada", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
partida = Button(segundo_frame, command=inicio ,text="iniciar outra partida", height=2, width=15, bg=cor_cinza, fg=cor_amarelo)
nomes = Label(segundo_frame, text="O jogo é humilde,\n porém, feito com muito\n esforço por: \n Bruno França\n Mariana Silva\n Priscilla\n Angelo Gabriel", height=8, relief=FLAT, anchor=CENTER,bg=cor_cinza, font=('Ivy 12 bold'), fg=cor_cian )
    
janela.mainloop()