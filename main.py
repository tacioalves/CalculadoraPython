from tkinter import *
from tkinter import ttk
from turtle import width

#Cores

preto = "#1e1f1e" #preta
branco = "#feffff" #branca
azul = "#38576b" #Azul
cizenta = "#ECEFF1" #cizenta
laranja = "#FFAB40" #laranja

#Frames
janela = Tk();
janela.title("Calculadora");
janela.geometry("235x310");
janela.config(bg=preto)

frame_tela = Frame(janela, width=235, height = 50, bg=azul);
frame_tela.grid(row=0, column=0);

frame_corpo = Frame(janela, width=235, height = 268);
frame_corpo.grid(row=1, column=0);


todos_valores = ""

#Função
def informa_Valores(event):

    global todos_valores

    todos_valores += str(event)
    #Passa valor
    valor_texto.set(todos_valores)


#Função resultado

def calcular():
    global todos_valores
    
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


#Função limpaTela

def limpa_tela():
    global todos_valores
    
    todos_valores=""
    valor_texto.set("")


#Criando Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto,width=16,height=2, padx=7, relief=FLAT, anchor="e",justify=RIGHT,font=("ivy 18"),bg=azul,fg=branco);
app_label.place(x=0,y=0)




#botões

#Linha 1
b_C = Button(frame_corpo, text="C", width=11, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE,fg=preto, command=lambda: limpa_tela());
b_C.place(x=0,y=0);
b_MODULO = Button(frame_corpo, text="%", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("%"));
b_MODULO.place(x=118,y=0);
b_DIVISAO = Button(frame_corpo, text="/", width=5, height=2,bg=laranja,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=branco, command=lambda: informa_Valores("/"));
b_DIVISAO.place(x=177,y=0);

#Linha 2
b_7 = Button(frame_corpo, text="7", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("7"));
b_7.place(x=0,y=52);
b_8 = Button(frame_corpo, text="8", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("8"));
b_8.place(x=59,y=52);
b_9 = Button(frame_corpo, text="9", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("9"));
b_9.place(x=118,y=52);
b_MULTIPLICA = Button(frame_corpo, text="*", width=5, height=2,bg=laranja,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=branco, command=lambda: informa_Valores("*"));
b_MULTIPLICA.place(x=177,y=52);


#Linha 3
b_4 = Button(frame_corpo, text="4", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("4"));
b_4.place(x=0,y=104);
b_5 = Button(frame_corpo, text="5", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("5"));
b_5.place(x=59,y=104);
b_6 = Button(frame_corpo, text="6", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("6"));
b_6.place(x=118,y=104);
b_SUBTRACAO = Button(frame_corpo, text="-", width=5, height=2,bg=laranja,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=branco, command=lambda: informa_Valores("-"));
b_SUBTRACAO.place(x=177,y=104);


#Linha 4
b_1 = Button(frame_corpo, text="1", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("1"));
b_1.place(x=0,y=156);
b_2 = Button(frame_corpo, text="2", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("2"));
b_2.place(x=59,y=156);
b_3 = Button(frame_corpo, text="3", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("3"));
b_3.place(x=118,y=156);
b_soma = Button(frame_corpo, text="+", width=5, height=2,bg=laranja,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=branco, command=lambda: informa_Valores("+"));
b_soma.place(x=177,y=156);


#Linha 5
b_0 = Button(frame_corpo, text="0", width=11, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE,fg=preto, command=lambda: informa_Valores("0"));
b_0.place(x=0,y=208);
b_ponto = Button(frame_corpo, text=".", width=5, height=2,bg=branco,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=preto, command=lambda: informa_Valores("."));
b_ponto.place(x=118,y=208);
b_igual = Button(frame_corpo, text="=", width=5, height=2,bg=laranja,font=("ivy 13 bold"),relief=RAISED,overrelief=RIDGE, fg=branco, command=lambda: calcular());
b_igual.place(x=177,y=208);




janela.mainloop();

