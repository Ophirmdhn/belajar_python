#Program list buku

list_buku = []

while (True) :

    judul = input('\nMasukan judul buku : ')
    penulis = input('Masukan nama penulis : ')

    #menggabungkan variabel
    buku = [judul, penulis]

    #memasukan input user kedalam list
    list_buku.append(buku)

    print('\nNo \t| Judul \t| Penulis')
    #menampilkan list
    for index,buku in enumerate(list_buku) :
        print(f'{index+1} \t| {buku[0]} \t| {buku[1]}')

    pilihan = input('\nIngin melanjutkan? (y/n) : ')
    if pilihan == 'n' :
        break

print('Terima Kasih')