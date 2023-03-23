import tkinter as tk
from tkinter import Label


class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg="black")
        self.master = master

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)


        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir archivo", command=self.open_file)
        self.file_menu.add_command(label="Guardar archivo", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, text="¡Hola, mundo!")
        self.label.pack(pady=20)
        self.button = tk.Button(self, text="Presionar", command=self.press_button)
        self.button.pack()
        self.pack()

    def open_file(self):
        l=Label(text="Abrir archivo")
        l.pack()

    def save_file(self):
       l=Label(text="Guardar archivo")
       l.pack()
    def quit_program(self):
        self.master.quit()

    def copy(self):
        l=Label(text="Copiar")
        l.pack()

    def paste(self):
        l=Label(text="Pegar")
        l.pack()

    def press_button(self):
        l=Label(text="Botón presionado")
        l.pack()


root = tk.Tk()
root.geometry("300x350")
root.wm_title("La bestia")
root.config(bg="black")
app = MenuScreen(root)
app.mainloop()