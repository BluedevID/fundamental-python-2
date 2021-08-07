"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = Kamus
"""

Kamus_ind_eng = {'anak': 'child', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(Kamus_ind_eng)
print(Kamus_ind_eng['anak'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_gojek = {
    'tanggal': '2021-8-7',
    'driver_list': [{'nama': 'Eko', 'jarak': 10}, {'nama': 'Dwi', 'jarak': 100}, {'nama': 'Tri', 'jarak': 500},
                    {'nama': 'Catur', 'jarak': 1000}]
}

print(data_dari_gojek)
print(f"\nDriver disekitar sini {data_dari_gojek['driver_list']}")
print(f"Driver #1 {data_dari_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_gojek['driver_list'][0]['jarak']} dari anda")
