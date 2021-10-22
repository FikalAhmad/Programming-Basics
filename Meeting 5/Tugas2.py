print(" GEROBAK FRIED CHICKEN ")
print("------------------------")
print("Kode JenisPotong  Harga")
print(" D       Dada     Rp2500")
print(" P       Paha     Rp2000")
print(" S       Sayap    Rp1500")
print("------------------------")


harga = 0

banyak_jenis = int(input("Masukkan Banyak Jenis Potong yang dipilih : "))
for i in range(banyak_jenis):
    print("Jenis Ke - " + str(i+1))
    kode_potong = input("Masukkan Kode Potong [D/P/S] : ")
    banyak_potong = int(input("Masukkan Banyak Potong : "))
    
    if kode_potong=="D" or kode_potong=="d":
        jenis_potong="Dada"
        harga=2500
    elif kode_potong=="P" or kode_potong=="p":
        jenis_potong="Paha"
        harga=2000
    elif kode_potong=="S" or kode_potong=="s":
        jenis_potong="Sayap"
        harga=1500
    else:
        kode_potong="Anda Salah Input Kode Potong"
        harga=0

    banyak_potong * harga


judul = "GEROBAK FRIED CHICKEN"
print(judul.center(70))
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("No.\tJenis Potong\tHarga Satuan\tBanyak Beli\tJumlah Harga")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")







print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

