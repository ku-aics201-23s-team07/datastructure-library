def heapify(scooters, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2 

    if l < n and scooters[l]["battery"] > scooters[largest]["battery"]:
        largest = l

    if r < n and scooters[r]["battery"] > scooters[largest]["battery"]:
        largest = r

    if largest != i:
        scooters[i], scooters[largest] = scooters[largest], scooters[i]
        heapify(scooters, n, largest)

def build_heap(scooters):
    n = len(scooters)
    for i in range(n//2 - 1, -1, -1):
        heapify(scooters, n, i)
    
    return scooters