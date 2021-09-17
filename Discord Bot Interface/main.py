from tkinter import *
from Functions import Buttons
from Functions import Labels
from Functions import InsertBoxs


def window_organize(window, name = 'Window', width = 1280, height = 720, resizable_width = False, resizable_height = False, min_width = 200, min_height = 200):
    '''
    -> Function to organizes your window
    :param window: Window param
    :param name: (Optional) Window name
    :param width: (Optional) Window width
    :param height: (Optional) Widnow height
    :param resizable_width: (Optional) If window width can resize
    :param resizable_height: (Optional) If window width can resize
    :param min_width: (Optional) Minimum value to resize width
    :param min_height: (Optional) Minimum value to resize height
    '''
    window.title(name)
    window.geometry(f'{width}x{height}')
    window.minsize(min_width, min_height)
    window.resizable(resizable_width, resizable_height)


window_layout = {'window_name': 'Discord Bot Interface',
        'width': 1280, 'height': 720,
        'min_width': 200, 'min_height': 200,
        'backgroud_color': 'white'}

window = Tk()
window_organize(window, window_layout['window_name'],
                window_layout['width'], window_layout['height'],
                min_width = window_layout['min_width'], min_height = window_layout['min_height'])


while True:
    # Button
    button_list = Buttons.Buttons(window)
    button_list[0].pack()
    button_list[1].pack()
    button_list[2].pack()
    button_list[2].place(bordermode=OUTSIDE, x = 0, y = window_layout['height'] - 30)

    # Label
    label_list = Labels.Labels(window)
    label_list[0].pack()
    label_list[0].place(bordermode=OUTSIDE, x = 20, y = 0)

    # Insert Box

    insert_box_list = InsertBoxs.insert_boxs(window)
    insert_box_list[0].pack()
    insert_box_list[0].place(bordermode=OUTSIDE, x = 60, y = window_layout['height'] - 26)


    InsertBoxs.get_insert_box(insert_box_list[0])


    window.mainloop()