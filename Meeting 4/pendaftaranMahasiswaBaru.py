nis = input("Masukkan NIS Anda : ")
nama = input("Masukkan Nama Anda : ")
jurusan = input("Masukkan Jurusan Anda [SI/SIA]: ")

if jurusan=="SI" or jurusan=="si":
    namajurusan="Sistem Informasi"
    harga=2400000
elif jurusan=="BL":
    namajurusan="Bali"
    harga=2000000
else :
    namajurusan="Anda Salah Input Kode Merk"
    harga=0

print("==============================")
print("NIS : "+str(nis))
print("Nama : "+str(nama))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga : ",+(harga))