import tkinter

def coletar():
    label2["text"] = f"Olá, {entrada.get()}!"
    entrada.delete(0, "end")

tela_principal = tkinter.Tk()
tela_principal.title("Tela de Login")
tela_principal.geometry("400x400")

label1 = tkinter.Label(tela_principal,
                       text="Digite seu nome e Sobrenome: ",
                       font=("arial",10))

entrada = tkinter.Entry(tela_principal,
                       width=35)
entrada.place(x=102, y=45)

label1.place(x=100, y=20)
botao1 = tkinter.Button(tela_principal, text="Ok",
                        activebackground="#696760",
                        activeforeground="#40e3d9",
                        bg="#9bc9c7",
                        font=("arial",8),
                        width=6,
                        height=1,
                        command=coletar)
botao1.place(x=150, y=70)

label2 = tkinter.Label(tela_principal,
                       font=("arial",10),
                       text="")
label2.place(x=100, y=120)

botao2 = tkinter.Button(tela_principal, text="Cancel",
                        activebackground="#696760",
                        activeforeground="#40e3d9",
                        bg="#9bc9c7",
                        font=("arial",8),
                        width=6,
                        height=1,
                        command=tela_principal.destroy)
botao2.place(x=100, y=70)

tela_principal.mainloop()