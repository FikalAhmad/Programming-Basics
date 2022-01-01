# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Uji Kompetensi ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
harga = 0
jumlah_harga = 0
df_jenis_studio = []
df_kode_studio = []
df_harga_satuan = []
df_banyak_beli = []
df_jumlah_harga = []

judul = '''PEMESANAN TIKET BIOSKOP "NUSSA" '''
print(judul)
print("---------------------------------------------")
tanggal_pemesanan = input("Tanggal Pemesanan : ")
nama_pemesan = input("Masukkan Nama Pemesan : ")
banyak_transaksi = int(input("Masukkan Jumlah Transaksi : "))
print()
print()

for i in range(banyak_transaksi):
    print("Transaksi Ke - " + str(i+1))
    kode_studio = input("Kode Studio [1/2/3/4] : ")
    banyak_studio = int(input("Masukkan Jumlah Tiket : "))
    print("---------------------------------------------")
    print()
    if kode_studio=="1":
        jenis_studio="Regular  "
        harga=30000
    elif kode_studio=="2":
        jenis_studio="VIP      "
        harga=45000
    elif kode_studio=="3":
        jenis_studio="VVIP     "
        harga=55000
    elif kode_studio=="4":
        jenis_studio="Eksklusif"
        harga=100000
    else:
        kode_studio="Anda Salah Input Kode Studio"
        harga=0

    df_jenis_studio.append(jenis_studio)
    df_kode_studio.append(kode_studio)
    df_harga_satuan.append(harga)
    df_banyak_beli.append(banyak_studio)
    df_jumlah_harga.append(banyak_studio * harga)

print()
judul = '''================== DATA PEMESANAN TIKET BIOSKOP "NUSSA" =================='''
print(judul.center(70))
print("Tanggal Pemesanan Tiket : ", (tanggal_pemesanan))
print("Nama Pemesan : ", (nama_pemesan))
print("==========================================================================")
print("No.\tKode Studio\tJenis Studio\tJumlah Tiket\tHarga\tSubtotal")
print("==========================================================================")
for i in range(0, banyak_transaksi):
    print("{0}\t{1}\t\t{2}\t{3}\t\t{4}\t{5}".format(i + 1,df_kode_studio[i],df_jenis_studio[i],df_banyak_beli[i],df_harga_satuan[i],df_jumlah_harga[i]))
print("==========================================================================")
for harga in (df_jumlah_harga):
    jumlah_harga = jumlah_harga + harga
print("Total : Rp.", jumlah_harga)
pajak = jumlah_harga * 10/100
print("Pajak : Rp.", pajak)
total_keseluruhan = (jumlah_harga + pajak)
print("Total Keseluruhan : Rp.", total_keseluruhan)
uang_bayar = int(input("Uang Bayar : "))
print("Uang Kembali : ", (uang_bayar-total_keseluruhan))