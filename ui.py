from tkinter import *
from tkinter import ttk

class CenterWidgetMixin:
    def center(self,):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry(f"{w}x{h}+{x}+{y}")


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Clientes')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ( 'dni','nombre', 'apellido' )
        treeview.pack()

        treeview.column('#0', width=0, stretch=NO)
        treeview.column('dni', anchor=CENTER)
        treeview.column('nombre', anchor=CENTER)
        treeview.column('apellido', anchor=CENTER)

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()