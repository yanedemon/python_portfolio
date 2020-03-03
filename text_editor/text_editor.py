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

def selectAll(event):
    window.after(10, select_all, event.widget)

def select_all(widget):
    widget.selection_range(0, END)
    widget.icursor(END)

window = tkinter.Tk()
window.title("Simple text editor")
window.minsize(width = 400, height = 400)
window.maxsize(width = 800, height = 800)
text = tkinter.Text(window, width = 100, height = 100, bg = 'black', fg = 'white', font = ('Trebuchet MS', 12))
text.pack(side = tkinter.LEFT)

# scroll = tkinter.Scrollbar(window, command = text.yview, orient = tkinter.VERTICAL)
# scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)

menuBar = tkinter.Menu(window)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label = 'Создать файл', command = create_new_file)
fileMenu.add_command(label = 'Открыть файл', command = open_file)
fileMenu.add_command(label = 'Сохранить', command = save_file)
fileMenu.add_command(label = 'Сохранить как', command = save_as)
fileMenu.add_command(label = 'Выход', command = window.quit)
menuBar.add_cascade(label = 'Файл', menu = fileMenu)

window.config(menu = menuBar)
# text.config(yscrollcommand = scroll.set)

select_all_hotkey = tkinter.Entry(width = 40)
select_all_hotkey.focus_set()
select_all_hotkey.pack()
select_all_hotkey.bind('<Control-a>', selectAll)

window.event_add('<<Copy>>', '<Control-ntilde>')
window.event_add('<<Paste>>', '<Control-igrave>')

window.mainloop()
