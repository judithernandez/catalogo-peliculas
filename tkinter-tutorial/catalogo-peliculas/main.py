import tkinter as tk
from client.gui import Frame, barra_menu

def main():

    # Create the main window 
    root = tk.Tk()
    root.title('Catálogo de películas')
    root.resizable(0, 0)
    
    barra_menu(root)   

    # Create a Frame
    app = Frame(root=root)

    app.mainloop()
        
if __name__ == '__main__':
    main()
