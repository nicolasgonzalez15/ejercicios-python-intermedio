# Tarea 1 - Conjuntos

# Devolver elementos de conjuntos A o B o en ambos

conjA1 = {1,2,3,4}
conjB1 = {1,3,5,6}
conjC1 = {1,3}

print(f"Los elementos que estan en A o B o en ambos son: {conjA1 | conjB1}.")

# Devolver elementos de conjuntos A y B 

print(f"Los elementos que estan solo en A o B son: {conjA1 & conjB1}.")

# Devolver elementos de conjuntos A o B, pero no en ambos

print(f"Los elementos que estan solo en A o B, pero no en ambos son: {conjA1.symmetric_difference(conjB1)}.")

# Devolver si el conjunto C es subconjunto de B:

print(f"C es subconjunto de B: {conjC1.issubset(conjB1)}.")

# Cantidad de elementos únicos de conjunto A - len()

conjT1 = {1,3,4,5,3,1}


print(f"Cantidad de elementos únicos de conjunto T1: {len(conjT1)}.")

# Cantidad de elementos únicos de conjunto A - bucle for


elementos_unicos = []

for elemento in conjT1:
    if elemento not in elementos_unicos:
        elementos_unicos.append(elemento)

conjSinRepetidos = set(elementos_unicos)

totalSinRepetidos = len(conjSinRepetidos)


print(f"Cantidad de elementos sin repetidos de conjunto T1: {totalSinRepetidos}")