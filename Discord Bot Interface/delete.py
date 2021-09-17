from tkinter import *


def button(msg):
        print(msg)


menu = {'window_name': 'Discord Bot Interface',
        'width': 1280, 'height': 720,
        'min_width': 200, 'min_height': 200,
        'backgroud_color': 'grey'}

init_menu = Tk()

init_menu.title(menu['window_name']) # Windows name
init_menu.geometry(f'{menu["width"]}x{menu["height"]}') # Window Size
init_menu.resizable(True, True) # Can User Resizable the Window?

init_menu.minsize(menu['min_width'], menu['min_height']) # MinSize that User can change

init_menu['bg'] = menu['backgroud_color'] # Changes Backgroud color


# Button

btn = Button(init_menu, text = 'Clicar', command = lambda: button('Clicou.'))
btn2 = Button(init_menu, text = 'Baixo', command = lambda: button('Clicou 2.'))


# Label

label1 = Label(init_menu, text = 'It is a label.')
label2 = Label(init_menu, text = 'It is a label 2.',
                bg = menu['backgroud_color'],
                fg = 'white',
                font = 'Arbery 20')


# Entry

'''Label(init_menu, text = 'Digite aqui:').grid(row = 0, sticky = W)
Label(init_menu, text = 'Digite aqui 2:').grid(row = 1, sticky = W)

entry = Entry(init_menu).grid(row = 0, column = 1)
entry2 = Entry(init_menu).grid(row = 1, column = 1)'''


# Pack

btn.pack()
btn2.pack()
label1.pack()
label2.pack()


init_menu.mainloop()

#init_menu.iconbitmap('D:/Visual Studio Projects/Discord-Bot-Interface/Discord Bot Interface/images/icon.ico') Icon