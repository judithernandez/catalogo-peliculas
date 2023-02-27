import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
        # tearoff=0 removes the dashed line from the menu
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Registro en BD')
    menu_inicio.add_command(label='Eliminar Registro en BD')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas',menu=menu_consultas)

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración',menu=menu_configuracion)

    menu_ayuda = tk.Menu(barra_menu, tearoff=0)  
    barra_menu.add_cascade(label='Ayuda',menu=menu_ayuda)

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack(fill=tk.BOTH, expand=1)
            # fill option added to make widget fill entire frame.
            # expand option added to expand widget, if user resizes frame.
        self.config(bg='lightblue')