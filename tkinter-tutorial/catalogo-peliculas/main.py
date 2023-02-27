import tkinter as tk

def main():

    # Create the main window 
    root = tk.Tk()
    root.title('Catálogo de películas')
    root.geometry('800x400')
    root.resizable(0, 0)
    

    # Create a Frame
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=1)
    frame.config(bg='lightblue')

    root.mainloop()
        
if __name__ == '__main__':
    main()
