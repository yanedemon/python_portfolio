import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = tkinter.NONE

def create_new_file():
    global filename
    filename = 'Безымянный'
    text.delete('1.0', tkinter.END)

def open_file():
    global filename
    input = open_file_dialog(mode = 'r')
    if input is None:
        return
    filename = input.name
    data = input.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def save_file():
    data = text.get('1.0', tkinter.END)
    save = open(filename, 'w')
    save.write(data)
    save.close()

def save_as():
    save = save_as_dialog(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title = 'Ошибка', message = 'Невозможно сохранить файл')

window = tkinter.Tk()
window.title("Simple text editor")
window.minsize(width = 20, height = 20)
window.maxsize(width = 1920, height = 1080)
text = tkinter.Text(window, width = 800, height = 600, bg = 'black', fg = 'white')
text.pack()
menuBar = tkinter.Menu(window)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label = 'Создать файл', command = create_new_file)
fileMenu.add_command(label = 'Открыть файл', command = open_file)
fileMenu.add_command(label = 'Сохранить', command = save_file)
fileMenu.add_command(label = 'Сохранить как', command = save_as)
fileMenu.add_separator()
fileMenu.add_command(label = 'Выход', command = window.quit)
menuBar.add_cascade(label = 'Файл', menu = fileMenu)
window.config(menu = menuBar)

window.mainloop()

## TODO: Добавить горячие клавиши;
##       добавить скроллбар;
##       глянуть как работают теги
