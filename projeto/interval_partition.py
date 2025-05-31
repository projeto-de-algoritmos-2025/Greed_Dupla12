import heapq

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
