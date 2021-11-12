# Menambahkan Anggota List

ganjil = [1, 3, 5, 7]
ganjil.append(9)
print(ganjil)
ganjil.extend([11,13,15])
print(ganjil)

# Kita juga bisa menggunakan operator + untuk menggabungkan dua list, dan operator * untuk melipatgandakan list.

genap = [2, 4, 6]
print(genap + [8, 10, 12])
print(['p', 'y'] * 2)