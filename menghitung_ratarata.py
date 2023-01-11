daftar_input = input("Masukan angka, pisahkan dengan tanda ',' : ")
list_angka = daftar_input.split(',')

#list untuk menampung input
daftar_baru = [int(x) for x in list_angka] #dicasting ke int

jumlah = 0

for angka in daftar_baru :
    jumlah += angka

#membagi total dari input dengan jumlah data yang di masukan
rata_rata = jumlah / len(daftar_baru)

#menampilan nilai terendah
for angka in daftar_baru :
    print(angka)
    
print('Nilai terendah = ', min(daftar_baru))
print('Nilai tertinggi = ', max(daftar_baru))
print('Nilai rata - rata = ', rata_rata)





