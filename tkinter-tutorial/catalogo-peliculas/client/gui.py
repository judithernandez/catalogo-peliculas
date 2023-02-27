import tkinter as tk
import customtkinter as ctk
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu)

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
        self.campos_pelicula()

    def campos_pelicula(self):
        # Labels
        self.label_titulo = tk.Label(self, text='Título: ')
        self.label_titulo.config(bg='lightblue', fg='black')
        self.label_titulo.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(bg='lightblue', fg='black')
        self.label_duracion.grid(row=1, column=0, sticky='e', padx=10, pady=10)

        self.label_categoria = tk.Label(self, text='Categoría: ')
        self.label_categoria.config(bg='lightblue', fg='black')
        self.label_categoria.grid(row=2, column=0, sticky='e', padx=10, pady=10)

        # Entrys
        self.entry_titulo = tk.Entry(self)
        self.entry_titulo.config(justify='center', width=30, state='disabled')
        self.entry_titulo.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(justify='center', width=30, state='disabled')
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.entry_categoria = tk.Entry(self)
        self.entry_categoria.config(justify='center', width=30, state='disabled')
        self.entry_categoria.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Buttons
        self.button_nuevo = ctk.CTkButton(self, text='Nueva Película', command=None, corner_radius=5, fg_color=("green", "white"))
        self.button_nuevo.grid(row=3, column=0, sticky='e', padx=10, pady=10)

        self.button_guardar = ctk.CTkButton(self, text='Guardar', command=None, corner_radius=5)
        self.button_guardar.grid(row=3, column=1, sticky='w', padx=10, pady=10)

        self.button_descartar = ctk.CTkButton(self, text='Descartar', command=None, corner_radius=5, fg_color=("red", "white"))
        self.button_descartar.grid(row=3, column=2, sticky='w', padx=10, pady=10)

