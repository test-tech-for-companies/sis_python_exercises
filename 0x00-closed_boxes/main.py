#!/usr/bin/env python3
"""
Entrypoint module
"""

desbloqueo = __import__('lockcaja').desbloqueo


caja = [[1], [2], [3], [4], []]
print(desbloqueo(caja))

caja = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(desbloqueo(caja))

caja = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(desbloqueo(caja))

caja = [[0]]
print(desbloqueo(caja))

# Stress test
caja = []
llaves = []
for __ in range(1, 100):
    llaves = []
    for num in range(1, 100):
        llaves.append(num)
    caja.append(llaves)

print(desbloqueo(caja))



