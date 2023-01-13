#aplikasi data mahasiswa

class Mahasiswa() :
    nama = None
    nim = None
    jurusan = None

data_mahasiswa = []

def mainMenu() :
    print('\n1. Tambahkan data Mahasiswa')
    print('2. Tampilkan data Mahasiswa')
    print('3. Cari data Mahasiswa')
    print('4. Hapus data mahasiswa')
    print('5. Keluar')

def tambahkan_mahasiswa() :
    mahasiswa = Mahasiswa()
    mahasiswa.nama = input('Masukan nama : ')
    mahasiswa.nim = input('Masukan nim : ')
    mahasiswa.jurusan = input('Masukan jurusan : ')

    data_mahasiswa.append(mahasiswa)

def tampilkan_mahasiswa() :
    print('=====Data Mahasiswa=====')
    print(f'No | Nama \t\t| NIM \t\t| Jurusan')
    no = 1
    for mahasiswa in data_mahasiswa :
        print(f'{no} | {mahasiswa.nama} \t| {mahasiswa.nim} \t| {mahasiswa.jurusan}')
        no += 1
    print()

def cari_mahasiswa():
    cari_nim = input('masukan NIM yang ingin dicari : ')
    index = 0

    for mahasiswa in data_mahasiswa :
        if mahasiswa.nim == cari_nim :
            print('Mahasiswa dengan NIM {} Ditemukan!'.format(cari_nim))
            print(f'{mahasiswa.nama} {mahasiswa.nim} {mahasiswa.jurusan}')

            return index
        index += 1
        
    print('Mahasiswa dengan NIM {} Tidak Ditemukan!'.format(cari_nim))
    return -1

def hapus_mahasiswa() :
    index_mahasiswa = cari_mahasiswa()
    if index_mahasiswa == 1 :
        return
    
    del data_mahasiswa[index_mahasiswa]

    
#fungsi main / awal program
while (True) :
    mainMenu()

    pilihMenu = int(input('Pilih menu : '))
    if pilihMenu == 1 :
        tambahkan_mahasiswa()
    elif pilihMenu == 2 :
        tampilkan_mahasiswa()
    elif pilihMenu == 3 :
        cari_mahasiswa()
    elif pilihMenu == 4 :
        hapus_mahasiswa()
    elif pilihMenu == 5 :
        break
    else :
        print('Menu Tidak Tersedia!')

print('Terima Kasih:)')