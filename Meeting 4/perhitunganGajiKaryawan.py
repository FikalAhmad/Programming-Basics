nama_karyawan = input("Nama Karyawan : ")
gol_jabatan = input("Golongan Jabatan : ")
pendidikan = input("Pendidikan : ")
jam_kerja = int(input("Jumlah Jam Kerja : "))

print("------------------------------------")
print("    PROGRAM HITUNG GAJI KARYAWAN    ")
print("------------------------------------")
print("Nama Karyawan : ",nama_karyawan)
print("Golongan Jabatan : ",gol_jabatan)
print("Pendidikan : ",pendidikan)
print("Jumlah Jam : ",jam_kerja)

# Ket Lain
gaji_pokok = 300000
tunjangan_jabatan = 0
tunjangan_pend = 0

# Tunjangan Jabatan
if gol_jabatan=="1" or gol_jabatan=="satu":
    nama_gol="Satu"
    persentase=5/100
elif gol_jabatan=="2" or gol_jabatan=="dua":
    nama_gol="Dua"
    persentase=10/100
elif gol_jabatan=="3" or gol_jabatan=="tiga":
    nama_gol="Tiga"
    persentase=15/100
else :
    gol_jabatan="Anda Salah Input Golongan Jabatan"
    persentase=0

tunjangan_jabatan = persentase * gaji_pokok

# Tunjangan Pendidikan
if pendidikan=="SMA" or pendidikan=="sma":
    nama_pend="SMA"
    persentase=2.5/100
elif pendidikan=="D1" or pendidikan=="d1":
    nama_pend="Diploma 1"
    persentase=5/100
elif pendidikan=="D3" or pendidikan=="d3":
    nama_pend="Diploma 3"
    persentase=20/100
elif pendidikan=="S1" or pendidikan=="s1":
    nama_pend="Sarjana 1"
    persentase=30/100
else:
    pendidikan="Anda Salah Input Pendidikan"
    persentase=0

tunjangan_pend = persentase * gaji_pokok

# Honor Lembur
honor_lembur = 0
jam_lembur = jam_kerja - 8

if jam_lembur > 0:
    honor_lembur = jam_lembur * 3500

tunjangan = tunjangan_jabatan + tunjangan_pend

# OUTPUT
print("------------------------------------")
print("Karyawan yang bernama ",nama_karyawan)
print("Honor yang diterima")
print("Tunjangan Jabatan : ",tunjangan_jabatan)
print("Tunjangan Pendidikan : ",tunjangan_pend)
print("Honor Lembur : ",honor_lembur)
print("Total Gaji : ",gaji_pokok + tunjangan + honor_lembur)
print("------------------------------------")
