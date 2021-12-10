# Argumen Default
def print_info( nama, usia = 17 ):
    '''Fungsi ini menampilkan info yang dimasukkan'''
    print("Nama: ", nama)
    print("Usia: ", usia)

# Memanggil Fungsi print_info
print_info( usia = 29, nama = "Galih" )

# Pemanggilan fungsi tidak menyediakan argumen usia
print_info( nama = "Galih" )