import tkinter as tk
import threading
import webbrowser
import os
from PIL import Image, ImageTk

class PetApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pet App")
        self.root.overrideredirect(True)  # Remove a moldura da janela
        self.root.geometry("150x150")  # Define as dimensões da imagem
        self.root.wm_attributes("-topmost", True)  # Mantém o app em foco
        self.root.wm_attributes("-transparentcolor", "white")  # Define a cor transparente

        # Carrega a imagem
        self.image = Image.open("pet.png")  # Substitua "pet.png" pelo nome da sua imagem
        self.image = self.image.convert("RGBA")  # Converte para RGBA para usar transparência

        # Redimensiona a imagem para 200x200
        self.image = self.image.resize((150, 150), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)

        # Cria um label para a imagem
        self.label = tk.Label(self.root, image=self.image, borderwidth=0, bg="white")  # Define o fundo do label como branco
        self.label.pack()
        self.label.bind("<Button-1>", self.open_link)  # Liga o clique esquerdo à função open_link
        self.label.bind("<Button-3>", self.show_options_menu)  # Liga o clique direito à função show_options_menu

        # Permite arrastar a janela
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.move_window)

        # Resto do código (mesmo que o anterior)
        # ...

    def open_link(self, event):
        def open_link_window():
            self.link_window = tk.Tk()
            self.link_window.title("Selecionar Link")

            self.link_entry = tk.Entry(self.link_window)
            self.link_entry.pack()

            self.open_folder_button = tk.Button(self.link_window, text="Abrir Pasta", command=self.open_folder)
            self.open_folder_button.pack()

            self.open_web_button = tk.Button(self.link_window, text="Abrir Link", command=self.open_web)
            self.open_web_button.pack()

        threading.Thread(target=open_link_window).start()

    def open_folder(self):
        folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        os.startfile(folder)

    def open_web(self):
        link = self.link_entry.get()
        webbrowser.open(link)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def move_window(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        x = self.root.winfo_x() + delta_x
        y = self.root.winfo_y() + delta_y
        self.root.geometry(f"+{x}+{y}")

    def show_options_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Abrir Link", command=self.open_link)
        menu.add_command(label="Abrir Pasta", command=self.open_folder)
        menu.add_separator()  # Adiciona um separador no menu
        menu.add_command(label="Fechar", command=self.root.destroy)  # Adiciona a opção de fechar
        menu.post(event.x_root, event.y_root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PetApp()
    app.run()