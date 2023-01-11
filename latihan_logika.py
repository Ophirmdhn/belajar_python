# latihan logika menggunakan komparasi

#1.angka lebih dari 0 kurang dari 5 lebih dari 8 kurang dari 11

inputAngka = float(input('\nMasukan angka > 0 < 5, > 8 < 11 : '))

lebihDari = (inputAngka > 0)
print('\nlebih dari 0 = ', lebihDari)

kurangDari = (inputAngka < 5)
print('kurang dari 5 = ', kurangDari)

danLebih = (inputAngka > 8)
print('lebih dari 8 = ', danLebih)

danKurang = (inputAngka < 11)
print('kurang dari 11 = ', danKurang)

hasil = lebihDari and kurangDari or danLebih and danKurang
print('Angka yang anda masukan adalah : ', hasil)
print()


#2. angka kurang dari 0 lebih dari 5 kurang dari 8 lebih dari 11

inputAngka = float(input('\nMasukan angka < 0 > 5 < 8 > 11 : '))

kurangDari = (inputAngka < 0)
print('Angka kurang dari 0 = ', kurangDari)

lebiDari = (inputAngka > 5)
print('Angka lebih dari 5 = ', lebiDari)

danKurang = (inputAngka < 8)
print('Angka kurang dari 8 = ', danKurang)

danLebih = (inputAngka > 11)
print('Angka lebih dari 11 = ',danLebih )

hasil = kurangDari or lebiDari and danKurang or danLebih
print('Angka yang anda masukan adalah : ',hasil)
print()