#TIPE DATA SKALAR => TIPE DATA SEDERHANA
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#TIPE DATA LIST/DAFTAR/ARRAY
anak = ['Eko', 'dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo') #append (Untuk menambahkan data dalam variabel)
print(anak)

#MEMANGGIL DATA VARIBEL TERTENTU
print(f'Hay {anak[2]}')

#MEMANGGIL SELURUH DATA
for a in anak:
    print(f'Hai {a}')

#MEMANGGI SELURUH DATA CARA RIBET
for a in range(0, len(anak)):
    print(f'hai {anak[a]}')