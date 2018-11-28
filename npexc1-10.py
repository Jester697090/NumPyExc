# Exc1
import numpy as np

print('Używana wersja biblioteki NumPy:', np.__version__)

# Exc2
a = np.arange(10)  # tablica liczb od 0 do 9
a = np.arange(2, 12, 2)  # tablica od 2 do 10 ze skokiem co 2
a = np.arange(2, 12, 2, dtype=float) # tablica liczb zmiennoprzecinkowych od 2 do 10 ze skokiem co 2
print(a)
print(type(a))

# Exc3
b = np.full((3, 3), True, dtype=bool)
print(b)
print(type(b))

# Exc4
c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(c[c % 2 == 1])  # indeksowanie logiczne, jak w matlabie

# Exc5
c[c % 2 == 1] = -1
print(c)

# Exc6
c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
d = np.where(c % 2 == 1, -1, c)
print(c)  # oryginał
print(d)  # zmieniona przy pomocy np.where()

# Exc7
e = np.arange(10)
print(e)
print(e.reshape(2, -1)) # ustawienie -1 pozwala funkcji automatycznie dobrać liczbę kolumn

# Exc8
print('Exc8')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

print(np.concatenate([a, b], axis=0))  # axis: 0 - w pionie, 1 - w poziomie
# print(cp.vstack([a, b]))
# print(np.r_[a, b])

# Exc9
print('Exc9')
print(np.concatenate([a, b], axis=1))
# print(np.hstack([a, b]))
# print(np.c_[a, b])

# Exc 10
print('Exc10')
c = np.array([1, 2, 3])
print(np.hstack([np.repeat(c, 3), np.tile(c, 3)]))