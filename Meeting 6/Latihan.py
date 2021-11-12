#variable yg berulang menggunakan List/matriks
list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]
tambah_data = ""
total_data = 0
while tambah_data != "n":
    ulang = int(input("Masukkan Data: "))
    for i in range(total_data, total_data + ulang):
        print ("data Ke - " + str(i+1))
        list_nim.append(input("Masukkan Nim anda : "))
        list_uts.append(int(input("Masukkan Nilai UTS anda :")))
        list_uas.append(int(input("Masukkan Nilai UAS : ")))
    
    #proses
    for i in range(ulang):
        list_total.append((list_uas[i] + list_uts[i]) / 2)

    tambah_data = input("Apakah anda ingin menambah data lagi? (y/n)")

    total_data = total_data + ulang


#Cetak
print("==============================================================")
print("Nim \t         Nilai Uts \t Nilai UAS \tTotal")
print("==============================================================")
for i in range(total_data):
    print ("%s \t %i \t\t %i \t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
print("==============================================================")
