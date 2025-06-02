import tkinter as tk
from tkinter import messagebox
import heapq

# Classe Aula para armazenar os dados
class Aula:
    def __init__(self, nome, inicio, fim):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim

    def __repr__(self):
        return f"{self.nome} ({self.inicio} - {self.fim})"

# Função do algoritmo
def interval_partition(aulas):
    aulas_ordenadas = sorted(aulas, key=lambda aula: aula.inicio)

    heap = []
    salas = {}
    prox_sala_id = 1

    for aula in aulas_ordenadas:
        if heap and heap[0][0] <= aula.inicio:
            fim_antigo, sala_id = heapq.heappop(heap)
            salas[sala_id].append(aula)
        else:
            sala_id = prox_sala_id
            prox_sala_id += 1
            salas[sala_id] = [aula]

        heapq.heappush(heap, (aula.fim, sala_id))

    return salas

# Lista para armazenar as aulas
aulas = []

# Função para adicionar aula
def adicionar_aula():
    nome = entry_nome.get()
    try:
        inicio = int(entry_inicio.get())
        fim = int(entry_fim.get())
    except ValueError:
        messagebox.showerror("Erro", "Horários devem ser números inteiros!")
        return

    if inicio >= fim:
        messagebox.showerror("Erro", "Horário de início deve ser menor que o de término!")
        return

    nova_aula = Aula(nome, inicio, fim)
    aulas.append(nova_aula)
    messagebox.showinfo("Aula adicionada", f"Aula '{nome}' adicionada com sucesso!")

    # Limpar os campos
    entry_nome.delete(0, tk.END)
    entry_inicio.delete(0, tk.END)
    entry_fim.delete(0, tk.END)

# Função para processar as aulas e mostrar resultado
def finalizar():
    if not aulas:
        messagebox.showwarning("Sem aulas", "Nenhuma aula foi adicionada.")
        return

    salas = interval_partition(aulas)

    resultado = f"Número mínimo de salas: {len(salas)}\n\n"
    for sala_id, aulas_sala in salas.items():
        resultado += f"Sala {sala_id}:\n"
        for aula in aulas_sala:
            resultado += f"  - {aula.nome}: {aula.inicio} - {aula.fim}\n"
        resultado += "\n"

    messagebox.showinfo("Resultado", resultado)

# Interface gráfica
root = tk.Tk()
root.title("Alocação de Aulas - Interval Partition")

# Nome
tk.Label(root, text="Nome da Aula:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

# Início
tk.Label(root, text="Horário de Início (ex: 8):").pack()
entry_inicio = tk.Entry(root)
entry_inicio.pack()

# Fim
tk.Label(root, text="Horário de Término (ex: 10):").pack()
entry_fim = tk.Entry(root)
entry_fim.pack()

# Botão Adicionar Aula
btn_adicionar = tk.Button(root, text="Adicionar Aula", command=adicionar_aula)
btn_adicionar.pack(pady=5)

# Botão Finalizar
btn_finalizar = tk.Button(root, text="Finalizar e Ver Alocação", command=finalizar)
btn_finalizar.pack(pady=5)

# Loop
root.mainloop()
