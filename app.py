import tkinter as tk
from tkinter import simpledialog, messagebox
from canvas_utils import on_mouse_click, calcular, apagar # type: ignore
from usuario import Usuario # type: ignore

def run_app():
    janela = tk.Tk()
    janela.title('Trabalho POO')

    usuario = None

    def cadastrar_usuario():
        nonlocal usuario
        nome = simpledialog.askstring("Cadastro de Usuário", "Digite seu nome:")
        if nome:
            usuario = Usuario(nome)
            messagebox.showinfo("Usuário Cadastrado", f"Usuário {nome} cadastrado com sucesso!")

    def calcular_funcao():
        if usuario:
            calcular(canvas, label_mostrar_funcao, usuario)
        else:
            messagebox.showwarning("Erro", "Por favor, cadastre um usuário primeiro.")

    def mostrar_usuario_funcao():
        if usuario and usuario.funcao:
            messagebox.showinfo("Usuário e Função", str(usuario))
        elif usuario:
            messagebox.showinfo("Usuário", f"Usuário: {usuario.nome} ainda não calculou nenhuma função.")
        else:
            messagebox.showwarning("Erro", "Por favor, cadastre um usuário primeiro.")

    canvas = tk.Canvas(janela, width=800, height=600)
    canvas.bind('<Button>', on_mouse_click)
    canvas.pack()

    label_mostrar_funcao = tk.Label(janela, text='Função:', font='arial 16')
    label_mostrar_funcao.pack()

    btn_cadastrar = tk.Button(janela, text='Cadastrar Usuário', font='arial 16', command=cadastrar_usuario)
    btn_cadastrar.pack()

    btn_calcular = tk.Button(janela, text='Calcular', font='arial 16', command=calcular_funcao)
    btn_calcular.pack()

    btn_apagar = tk.Button(janela, text='Apagar', font='arial 16', command=lambda: apagar(canvas, label_mostrar_funcao))
    btn_apagar.pack()

    btn_mostrar_usuario_funcao = tk.Button(janela, text='Mostrar Usuário e Função', font='arial 16', command=mostrar_usuario_funcao)
    btn_mostrar_usuario_funcao.pack()

    janela.mainloop()
