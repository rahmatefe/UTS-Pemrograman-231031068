''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']
#(NOTED: sesuaikan dengan data anda)

2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

# Definisikan variabel Bio
Bio = ['Institut Teknologi Bacharuddin Jusuf Habibie', 'Parepare', 'Jurusan Sains', 'RAHMAT EFENDI', '231031068', '01-MEI-2005', 'S1', 'Sistem Informasi C', 'Aktif', 'ganjil', '2023-2024', 'KARTU HASIL STUDI MAHASISWA']

# Definisikan variabel nested list MK
MK = [['Pendiikan Agama Islam', 'Pancasila', 'Bahasa Indonesia', 'Wawasan Cinta Iptek dan Imtaq', 'Pengantar Pemograman', 'Pengantar Teknologi Informasi', 'Kalkulus Dasar I', 'Sains Terpadu'],
      [2, 2, 2, 2, 3, 3, 3, 3],
      ['22A1209', '22A1210', '22A1211', '22A1212', '22A1213', '22A1214', '22A1215', '22A1216'],
      [3.50, 3.00, 3.75, 4.00, 3.75, 3.50, 3.75, 3.00]]

# Susun kode untuk menampilkan hasil seperti yang diinginkan
print(f"\n{' ' * ((75 - len(Bio[0])) // 2)}{Bio[0]}")
print(f"{' ' * ((70 - len(Bio[2])) // 2)}{Bio[2]}")
print(f"{' ' * ((50 - len(Bio[9])) // 2)}{'/'.join(Bio[11].split('-'))}")
print(f"{' ' * ((60 - len(Bio[9])) // 2)}{Bio[9].capitalize()} {Bio[10]} ")
print()


print(f"{'Nama Lengkap':<20} : {Bio[3].upper()}")
print(f"{'NIM':<20} : {Bio[4]}")
print(f"{'TTL':<20} : {Bio[5]}")
print(f"{'Program/Prodi':<20} : {Bio[6]}/{Bio[7]}")
print(f"{'Tahun Masuk':<20} : {Bio[10]}")
print(f"{'Status':<20} : {Bio[8]}\n")


# Header tabel MK
print(f"{'|--|--   12   --|--             31            --|-- 7 --|--    13   --|'}")
print('-' * 70)

print(f"No. Kode\t|\tMata Kuliah\t|\t SKS  | Nilai (0-4) |")

print(f"1   {MK[-2][0]}\t| {MK[0][0]}\t\t|   {MK[1][0]}   |\t  {MK[-1][0]}0|")
print(f"2   {MK[-2][1]}\t| {MK[0][1]}\t\t        |   {MK[1][1]}   |\t  {MK[-1][1]}0|")
print(f"3   {MK[-2][2]}\t| {MK[0][2]}\t\t|   {MK[1][2]}   |\t  {MK[-1][2]}|")
print(f"4   {MK[-2][3]}\t| {MK[0][3]}\t|   {MK[1][3]}   |\t  {MK[-1][3]}0|")
print(f"5   {MK[-2][4]}\t| {MK[0][4]}\t\t|   {MK[1][4]}   |\t  {MK[-1][4]}|")
print(f"6   {MK[-2][5]}\t| {MK[0][5]}\t|   {MK[1][5]}   |\t  {MK[-1][5]}0|")
print(f"7   {MK[-2][6]}\t| {MK[0][6]}\t\t|   {MK[1][6]}   |\t  {MK[-1][6]}|")
print(f"8   {MK[-2][7]}\t| {MK[0][7]}\t\t        |   {MK[1][7]}   |\t  {MK[-1][7]}0|")


print('-' * 70)
print(f"\t\t\t\t       TOTAL SKS:   {sum(MK[1])}")
print('-' * 70)

# Summary
pt = 70
a = "71"
print(f"|{a.center(pt,'-')}|")
print("Summary:")
print(f"Jumlah Mata Kuliah\t: {len(MK[0])} Mata Kuliah")
print(f"Nilai Tertinggi\t\t: {max(MK[-1])}0 ({MK[-2][3]} - {MK[0][3]})")
print(f"Nilai Terendah\t\t: {min(MK[-1])}0 ({MK[-2][-1]} - {MK[0][-1]})")
print("IP Kumulatif\t\t: 3.00")

print(f"{'Parepare, 26 Oktober 2023':>70}\n")
print(f"\n{'RAHMAT EFENDI':>70}\n{'-' * 70}")