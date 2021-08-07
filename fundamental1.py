#KONSTRUKSI DASAR PYTHON
#SEQUENTIAL : Eksekusi berurutan
print('Hello World!')
print('By Anggi Permata Adian')
print('Tanggal 6 Agustus 2021')
print('-' * 10)


#PERCABANGAN: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('Jalan lurus!')
else:
    print('Jalan lain')

#PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1):
    print(f'Halo anak #{index_anak}')
