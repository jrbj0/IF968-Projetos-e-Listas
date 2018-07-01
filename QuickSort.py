def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end
    done = 0
    while not done:
        while not done:
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break
            if list[bottom] > pivot:
                list[top] = list[bottom]
                break

    while not done:
        top = top-1
        if top == bottom:
            done = 1
            break
        if list[top] < pivot:
            list[bottom] = list[top]
            break
    list[top] = pivot
    return top

def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return list


















def quick(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[int(len(lista)/2)]
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivo:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        menores = quick(lista[:i])
        maiores = quick(lista[i+1:])
            
        return menores + [lista[i]] + maiores
    

from time import clock

lista = [125, 75, 36, 48, 65, 150, 1, 65, 90]

print(quick(lista))














