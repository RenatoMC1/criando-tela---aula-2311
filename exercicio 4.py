import tkinter
import random



# lista = []
#
# for i in range(1,61):
#     lista.append(i)
#
# print(lista)
# print(random.sample(lista, k=6))

tela_principal = tkinter.Tk()
tela_principal.title("Números")
tela_principal.geometry("400x400")

label1 = tkinter.Label(tela_principal,
                       text="Números sorteados: ",
                       font=("arial",10))

label1.place(x=100, y=20)
botao1 = tkinter.Button(tela_principal, text="Gerar",
                        activebackground="#696760",
                        activeforeground="#40e3d9",
                        bg="#9bc9c7",
                        font=("arial",8),
                        width=6,
                        height=1)
botao1.place(x=150, y=70)

tela_principal.mainloop()