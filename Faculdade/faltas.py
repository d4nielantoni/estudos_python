import tkinter as tk
from tkinter import messagebox

class GerenciadorDeFaltasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Faltas por Matéria")
        self.root.geometry("600x650")

        self.materias = {}  # Dicionário para armazenar matérias
        self.dark_mode = False  

        # Botão para alternar Dark Mode
        self.toggle_dark_mode_button = tk.Button(root, text="🌙", command=self.toggle_dark_mode, font=("Arial", 12))
        self.toggle_dark_mode_button.pack(pady=10)

        self.label_materia = tk.Label(root, text="Nome da Matéria:", font=("Arial", 12))
        self.label_materia.pack(pady=5)

        self.entry_materia = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_materia.pack(pady=5)

        self.label_carga_horaria = tk.Label(root, text="Carga Horária (em horas):", font=("Arial", 12))
        self.label_carga_horaria.pack(pady=5)

        self.entry_carga_horaria = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_carga_horaria.pack(pady=5)

        self.add_materia_button = tk.Button(root, text="Adicionar Matéria", command=self.adicionar_materia, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_materia_button.pack(pady=10)

        self.materia_list_label = tk.Label(root, text="Matérias Cadastradas:", font=("Arial", 12, "bold"))
        self.materia_list_label.pack(pady=5)

        self.materia_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=6)
        self.materia_listbox.pack(pady=5)

        self.label_faltas = tk.Label(root, text="Adicionar Faltas para a Matéria Selecionada:", font=("Arial", 12))
        self.label_faltas.pack(pady=5)

        self.entry_faltas = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_faltas.pack(pady=5)

        self.add_faltas_button = tk.Button(root, text="Adicionar Faltas", command=self.adicionar_faltas, font=("Arial", 12), bg="#007BFF", fg="white")
        self.add_faltas_button.pack(pady=10)

        self.view_faltas_button = tk.Button(root, text="Visualizar Faltas", command=self.visualizar_faltas, font=("Arial", 12), bg="#FFC107", fg="black")
        self.view_faltas_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Sair", command=root.quit, font=("Arial", 12), bg="#FF5722", fg="white")
        self.quit_button.pack(pady=10)

        # Pré-cadastro das minhas matérias
        self.pre_cadastro_materias()

    def pre_cadastro_materias(self):
        materias_pre_cadastradas = {
            "Inteligência Artificial": 72,
            "Banco de Dados": 72,
            "Design e Arquitetura": 72,
            "Sistemas Operacionais": 36,
            "Inglês": 36
        }
        for nome_materia, carga_horaria in materias_pre_cadastradas.items():
            self.materias[nome_materia] = {
                'carga_horaria': carga_horaria,
                'faltas': 0,
                'limite_faltas': int(0.25 * carga_horaria)  # Limite de 25%
            }
            self.materia_listbox.insert(tk.END, nome_materia)

    def adicionar_materia(self):
        nome_materia = self.entry_materia.get().strip()
        try:
            carga_horaria = int(self.entry_carga_horaria.get().strip())
            if not nome_materia or carga_horaria <= 0:
                raise ValueError("Dados inválidos.")
            
            if nome_materia in self.materias:
                messagebox.showerror("Erro", f"A matéria '{nome_materia}' já foi adicionada.")
                return

            self.materias[nome_materia] = {
                'carga_horaria': carga_horaria,
                'faltas': 0,
                'limite_faltas': int(0.25 * carga_horaria)  # Limite de 25%
            }
            self.materia_listbox.insert(tk.END, nome_materia)
            messagebox.showinfo("Sucesso", f"Matéria '{nome_materia}' adicionada com carga horária de {carga_horaria} horas.")
            self.entry_materia.delete(0, tk.END)
            self.entry_carga_horaria.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um nome válido e uma carga horária numérica positiva.")

    def adicionar_faltas(self):
        try:
            selected_index = self.materia_listbox.curselection()
            if not selected_index:
                messagebox.showerror("Erro", "Por favor, selecione uma matéria para adicionar faltas.")
                return

            nome_materia = self.materia_listbox.get(selected_index)
            faltas = int(self.entry_faltas.get().strip())
            if faltas <= 0:
                raise ValueError("O número de faltas deve ser positivo.")

            materia_info = self.materias[nome_materia]
            if materia_info['faltas'] + faltas > materia_info['limite_faltas']:
                messagebox.showerror("Limite Excedido", f"Não é possível adicionar {faltas} falta(s). Isso excederia o limite de {materia_info['limite_faltas']} faltas para '{nome_materia}'.")
            else:
                materia_info['faltas'] += faltas
                messagebox.showinfo("Sucesso", f"{faltas} falta(s) adicionada(s) para '{nome_materia}'. Faltas totais: {materia_info['faltas']} de {materia_info['limite_faltas']} permitidas.")
                self.entry_faltas.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de faltas.")

    def visualizar_faltas(self):
        selected_index = self.materia_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro", "Por favor, selecione uma matéria para visualizar faltas.")
            return

        nome_materia = self.materia_listbox.get(selected_index)
        materia_info = self.materias[nome_materia]
        faltas_restantes = materia_info['limite_faltas'] - materia_info['faltas']
        faltas_texto = (f"Matéria: {nome_materia}\n"
                        f"Faltas atuais: {materia_info['faltas']}\n"
                        f"Limite de faltas: {materia_info['limite_faltas']}\n"
                        f"Faltas restantes: {faltas_restantes}")
        messagebox.showinfo("Status de Faltas", faltas_texto)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.root.configure(bg="#2E2E2E")
            self.toggle_dark_mode_button.config(text="☀️", bg="#444", fg="white")
            widgets = [self.label_materia, self.label_carga_horaria, self.materia_list_label, self.label_faltas]
            for widget in widgets:
                widget.config(bg="#2E2E2E", fg="white")
            self.entry_materia.config(bg="#555", fg="white", insertbackground="white")
            self.entry_carga_horaria.config(bg="#555", fg="white", insertbackground="white")
            self.entry_faltas.config(bg="#555", fg="white", insertbackground="white")
            self.materia_listbox.config(bg="#555", fg="white")
        else:
            self.root.configure(bg="SystemButtonFace")
            self.toggle_dark_mode_button.config(text="🌙", bg="SystemButtonFace", fg="black")
            widgets = [self.label_materia, self.label_carga_horaria, self.materia_list_label, self.label_faltas]
            for widget in widgets:
                widget.config(bg="SystemButtonFace", fg="black")
            self.entry_materia.config(bg="white", fg="black", insertbackground="black")
            self.entry_carga_horaria.config(bg="white", fg="black", insertbackground="black")
            self.entry_faltas.config(bg="white", fg="black", insertbackground="black")
            self.materia_listbox.config(bg="white", fg="black")

root = tk.Tk()
app = GerenciadorDeFaltasApp(root)
root.mainloop()

