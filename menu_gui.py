import os
import subprocess
import tkinter as tk
from tkinter import messagebox

class MenuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Navegador de Exercícios - Curso Python")
        self.root.geometry("600x450")
        
        # Começa no diretório atual
        self.current_directory = os.getcwd()
        self.base_directory = self.current_directory  # Define a raiz do projeto
        
        # Componente de texto para mostrar o caminho atual
        self.lbl_path = tk.Label(root, text=self.current_directory, fg="blue", wraplength=580, font=("Arial", 10, "italic"))
        self.lbl_path.pack(pady=10)
        
        # Campo de busca em tempo real
        search_frame = tk.Frame(root)
        search_frame.pack(fill=tk.X, padx=20, pady=5)
        tk.Label(search_frame, text="🔍 Pesquisar:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.filter_items) # Executa ao digitar
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 11))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Frame que vai guardar a lista e a barra de rolagem
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Lista (Listbox) onde os arquivos aparecerão
        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, font=("Consolas", 12))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Define que dois cliques executam a ação de abrir a pasta ou rodar o arquivo
        self.listbox.bind('<Double-Button-1>', self.on_double_click)
        
        # Botão para voltar ao diretório anterior
        self.btn_back = tk.Button(root, text="⬆ Voltar Diretório (..)", command=self.go_back, font=("Arial", 11, "bold"))
        self.btn_back.pack(pady=10)
        
        # Carrega os arquivos na inicialização
        self.load_directory()

    def load_directory(self):
        """Lê o diretório atual e adiciona pastas e arquivos na interface."""
        self.listbox.delete(0, tk.END)
        self.lbl_path.config(text=self.current_directory)
        
        try:
            raw_items = os.listdir(self.current_directory)
            self.all_current_items = [] # Guardará todos os itens da pasta antes da busca
            
            for item in raw_items:
                full_path = os.path.join(self.current_directory, item)
                
                # Filtro na pasta principal: mostrar apenas Python1, 2 e 3
                if self.current_directory == self.base_directory:
                    if item not in ["Python1 - 01 ao 35", "Python2 - 36 ao 71", "Python3 - 72 ao 114"]:
                        continue
                else:
                    # Nas subpastas: mostrar apenas arquivos .py ou outras pastas
                    if not (os.path.isdir(full_path) or item.endswith(".py")):
                        continue
                        
                self.all_current_items.append(item)
            
            # Limpa o campo de busca ao entrar na pasta e aplica os ícones
            self.search_var.set("")
            self.filter_items()
            
        except PermissionError:
            messagebox.showerror("Erro", "Sem permissão para acessar este diretório.")
            self.go_back()

    def filter_items(self, *args):
        """Filtra a exibição do Listbox baseando-se no que foi digitado na barra de busca."""
        self.listbox.delete(0, tk.END)
        self.items = []
        query = self.search_var.get().lower()
        
        for item in getattr(self, 'all_current_items', []):
            if query in item.lower(): # Verifica se o texto digitado faz parte do nome do arquivo
                self.items.append(item)
                full_path = os.path.join(self.current_directory, item)
                if os.path.isdir(full_path):
                    self.listbox.insert(tk.END, f"📁 {item}")
                elif item.endswith(".py"):
                    self.listbox.insert(tk.END, f"🐍 {item}")
                else:
                    self.listbox.insert(tk.END, f"📄 {item}")

    def on_double_click(self, event):
        """Ação acionada ao dar dois cliques em um item da lista."""
        selection = self.listbox.curselection()
        if not selection:
            return
            
        index = selection[0]
        selected_item = self.items[index]
        full_path = os.path.join(self.current_directory, selected_item)
        
        if os.path.isdir(full_path):
            self.current_directory = full_path
            self.load_directory()
        elif full_path.endswith(".py"):
            self.run_program(full_path)
        else:
            messagebox.showinfo("Aviso", "Por favor, selecione uma pasta ou um arquivo Python (.py).")

    def go_back(self):
        """Sobe um nível na árvore de diretórios."""
        if self.current_directory == self.base_directory:
            return # Impede de subir além da pasta principal do projeto
            
        parent_dir = os.path.dirname(self.current_directory)
        if parent_dir != self.current_directory:
            self.current_directory = parent_dir
            self.load_directory()

    def run_program(self, path):
        """Abre uma janela de Prompt de Comando (cmd) rodando o exercício e pausa no fim."""
        if os.name == 'nt': # Verifica se é Windows
            command = f'start cmd /c "python "{path}" & echo. & pause"'
            subprocess.Popen(command, shell=True)
        else:
            messagebox.showwarning("Aviso", "A execução em nova janela só está configurada para Windows.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuGUI(root)
    root.mainloop()