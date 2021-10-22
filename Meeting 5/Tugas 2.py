print(" GEROBAK FRIED CHICKEN ")
print("------------------------")
print("Kode JenisPotong  Harga")
print(" D       Dada     Rp2500")
print(" P       Paha     Rp2000")
print(" S       Sayap    Rp1500")
print("------------------------")

harga = 0
jumlah_harga = 0
df_jenis_potong = []
df_harga_satuan = []
df_banyak_beli = []
df_jumlah_harga = []

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
    df_jenis_potong.append(jenis_potong)
    df_harga_satuan.append(harga)
    df_banyak_beli.append(banyak_potong)
    df_jumlah_harga.append(banyak_potong * harga)

        
judul = "GEROBAK FRIED CHICKEN"
print(judul.center(70))
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("No.\tJenis Potong\tHarga Satuan\tBanyak Beli\tJumlah Harga")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
for i in range(0, banyak_jenis):
    print("{0}\t{1}\t\t{2}\t\t{3}\t\t{4}".format(i + 1, df_jenis_potong[i], df_harga_satuan[i], df_banyak_beli[i], df_jumlah_harga[i]))
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
for harga in (df_jumlah_harga):
    jumlah_harga = jumlah_harga + harga
print("                                          Jumlah Harga : Rp.", jumlah_harga)
pajak = jumlah_harga * 10/100
print("                                          Pajak 10% : Rp.", pajak)
print("                                          Total Bayar : Rp.", jumlah_harga + pajak)
