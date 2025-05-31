from aula import Aula
from interval_partition import interval_partition

def main():
    aulas = []

    print("Adicione as aulas (digite 'fim' para terminar):")
    while True:
        nome = input("Nome da aula: ")
        if nome.lower() == 'fim':
            break
        try:
            inicio = float(input("Início (ex: 8.5 para 08:30): "))
            fim = float(input("Fim (ex: 10.0 para 10:00): "))
            aulas.append(Aula(nome, inicio, fim))
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    if not aulas:
        print("Nenhuma aula cadastrada.")
        return

    salas = interval_partition(aulas)

    print(f"\nTotal de salas necessárias: {len(salas)}\n")
    for sala_id, aulas_na_sala in salas.items():
        print(f"Sala {sala_id}: {', '.join(str(aula) for aula in aulas_na_sala)}")

if __name__ == "__main__":
    main()
