import tkinter as tk
from usuario import Usuario  # type: ignore 

coordenadas_x = []
coordenadas_y = []
x_quadrado = []
x_y = []

def on_mouse_click(event):
    x, y = event.x, event.y
    ponto = event.widget.create_oval(x-5, y-5, x+5, y+5, fill='black')
    coordenadas_x.append(x)
    coordenadas_y.append(y)
    x_quadrado.append(x**2)
    x_y.append(x*y)

def calcular(canvas, label_mostrar_funcao, usuario: Usuario):
    a = (len(x_y) * sum(x_y) - sum(coordenadas_x) * sum(coordenadas_y)) / (len(x_quadrado) * sum(x_quadrado) - (sum(coordenadas_x)) ** 2)
    b = (sum(coordenadas_y) / len(coordenadas_y)) - a * (sum(coordenadas_x) / len(coordenadas_x))
    x_max = max(coordenadas_x)
    x_min = min(coordenadas_x)
    reta = canvas.create_line(x_min, a * x_min + b, x_max, a * x_max + b, width=5)
    funcao_str = f'F(x)={a:.2f}X + {b:.2f}'
    label_mostrar_funcao['text'] = funcao_str
    usuario.salvar_funcao(funcao_str)

def apagar(canvas, label_mostrar_funcao):
    coordenadas_x.clear()
    coordenadas_y.clear()
    x_quadrado.clear()
    x_y.clear()
    canvas.delete(tk.ALL)
    label_mostrar_funcao['text'] = 'Função:'
