from tabulate import tabulate

table = [[1,2,3], [4,5,6], [7,8,9], [0]]
print(tabulate(table, tablefmt='fancy_grid'))

print("Baris Pertama, Kolom Pertama: ", table[0][0])
print("Baris Pertama, Kolom Kedua: ", table[0][1])
print("Baris Pertama, Kolom Ketiga: ", table[0][2])
print("Baris Ketiga, Kolom Ketiga: ", table[2][2])
print("Baris Ke Empat, Kolom Pertama: ", table[3][0])
