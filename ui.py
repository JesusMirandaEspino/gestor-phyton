from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Clientes')
        self.build()

    def build(self):
        button = Button(self,text='Hola Mundo', command=self.hola)
        button.pack()

    def hola(self):
        print('Hola Mundo')

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()