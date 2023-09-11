#menghitung nilai rata rata tugas 4
angka = int(input("masukan banyak data yang akan dihitung ="))
print()
data = []
jum = 0
for i in range(0, angka):
    temp = int(input("masukan jumlah data ke-%d = "%(i+1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum/angka
print("\nRata-rata = %0.2f" %rata2)

