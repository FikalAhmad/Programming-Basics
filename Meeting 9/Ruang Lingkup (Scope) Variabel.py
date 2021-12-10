# Variabel Global
# Definisi Fungsi
def sum( arg1, arg2 ):
    '''Menambahkan variabel dan mengembalikan hasilnya.'''
    total = arg1 + arg2;
    # total disini adalah variabel lokal
    print("Di dalam fungsi nilai total : ", total)
    return total

# Pemanggilan fungsi sum
sum( 10, 20 )

print ("Di luar fungsi, nilai total : ", total)