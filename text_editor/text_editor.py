from tkinter import *
from tkinter import filedialog, ttk
import os

class App():
    def __init__(self):
        title = 'Новый документ'
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title(title)
        self.tabs = {'ky': 0}
        self.tab_list = []
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand = True, fill = 'both')
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = 'Создать', command = self.generate_tab)
        filemenu.add_command(label = 'Открыть', command = self.open_file)
        filemenu.add_command(label = 'Сохранить', command = self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label = 'Выйти', command = self.root.quit)
        menubar.add_cascade(label = 'Файл', menu = filemenu)
        editmenu = Menu(menubar, tearoff = 0)
        editmenu.add_command(label = 'Отменить')
        editmenu.add_command(label = 'Повторить')
        editmenu.add_separator()
        menubar.add_cascade(label = 'Правка', menu = editmenu)
        self.root.config(menu = menubar)

    def open_file(self):
        file = open(filedialog.askopenfilename(), 'r+')
        text_value = file.read()
        self.textWidget.delete(1.0, 'end-1c')
        self.textWidget.insert('end-1c', text_value)
        title = os.path.basename(file.name)
        self.root.title(title)
        file.close()

    def add_tab(self, name):
        tab = Tab(self.notebook, name)
        print(name)
        self.notebook.add(tab, text = name)
        self.tab_list.append(tab)

    def save_file(self):
        tab_to_save = self.get_tab()
        print(tab_to_save)
        tab_to_save.save_tab()

    def get_tab(self):
        print(self.notebook.index('current'))
        tab = self.tab_list[self.notebook.index('current')]
        return tab

    def generate_tab(self):
        if self.tabs['ky'] < 20:
            self.tabs['ky'] += 1
            self.add_tab('Документ ' + str(self.tabs['ky']))

    def run(self):
        self.root.mainloop()

class Tab(Frame):
    def __init__(self, root, name):
        Frame.__init__(self, root)
        self.root = root
        self.name = name
        self.textWidget = Text(self, font = ('Trebuchet MS', 12))
        self.textWidget.pack(expand = True, fill = 'both')

    def save_tab(self):
        print(self.textWidget.get('1.0', 'end-1c'))
        file = open(filedialog.asksaveasfilename() + '.txt', 'w+')
        file.write(self.textWidget.get('1.0', 'end-1c'))
        print(os.path.basename(file.name))
        title = os.path.basename(file.name)
        file.close()

if __name__ == '__main__':
    app1 = App()
    app1.run()
