from tkinter import *
from Functions import InsertBoxs


def Buttons(window):
    print('Buttons')

    button_list = [Button(window, text = 'Clicar', command = lambda: Clicar()),
                    Button(window, text = 'Baixo', command = lambda: Baixo()),
                    Button(window, text = 'Connect', command = lambda: Connect(window))]

    return button_list




def Clicar():
    print('Clicar')


def Baixo():
    print('Baixo')


def Connect(window):
    print('Conectando...')