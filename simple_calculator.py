#kalkulator sederhana

#mainscreen
print('')
print('a. Tambah (+)')
print('b. Kurang (-)')
print('c. Kali (x)')
print('d. Bagi (/)')
print('e. Pangkat')

operator = str(input('Pilih Operator : '))

angka1 = int(input('Masukan angka pertama : '))
angka2 = int(input('Masukan angka kedua : '))

if (operator == 'a') :
    hasil = angka1 + angka2
    print('hasil dari', angka1, '+', angka2, '=', hasil)

elif (operator == 'b') :
    hasil = angka1 - angka2
    print('hasil dari', angka1, '-', angka2, '=', hasil)

elif (operator == 'c') :
    hasil = angka1 * angka2
    print('hasil dari', angka1, 'x', angka2, '=', hasil)

elif (operator == 'd') :
    hasil = angka1 / angka2
    print('hasil dari {} / {} = {}'.format(angka1, angka2, hasil))
    #menggunakan print format

elif (operator == 'e') :
    hasil = angka1 ** angka2
    print('hasil dari {} Pangkat {} = {}' .format(angka1, angka2, hasil))

else :
    print('Operasi Ridak Tersedia')
    