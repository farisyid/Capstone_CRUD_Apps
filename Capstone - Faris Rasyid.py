from tabulate import tabulate

pasien = [
    {
        'Nama': 'Bambang',
        'Jenis Kelamin': 'Pria',
        'Umur': 43,
        'Keluhan': 'Sesak Napas',
        'Tensi Darah': '80/21',
        'Kategori Triage': 'Merah'
    },
    {
        'Nama': 'Tri',
        'Jenis Kelamin': 'Pria',
        'Umur': 51,
        'Keluhan': 'Patah Tulang',
        'Tensi Darah': '80/21',
        'Kategori Triage': 'Merah'
    },
    {
        'Nama': 'Darmo',
        'Jenis Kelamin': 'Pria',
        'Umur': 34,
        'Keluhan': 'Sesak Napas',
        'Tensi Darah': '80/21',
        'Kategori Triage': 'Kuning'
    }
]

def tabelpasien():
    headers=['No','Nama','Jenis Kelamin','Umur','Keluhan','Tensi Darah','Kategori Triage']
    tabeldata=[[i+1,j['Nama'],j['Jenis Kelamin'],j['Umur'],j['Keluhan'],j['Tensi Darah'],j['Kategori Triage'],] for i,j in enumerate(pasien)]
    table=tabulate(tabeldata,headers=headers,tablefmt='grid')
    print(table)

def pasienbaru():
    Nnamapasien = input('Nama Pasien : ')
    Njeniskelamin = input('Jenis Kelamin : ')
    Numur = int(input('Umur : '))
    Nkeluhan = input('Keluhan : ')
    Ntensidarah = input('Tensi Darah : ')
    pasien.append({
            'Nama': Nnamapasien.capitalize(),
            'Jenis Kelamin': Njeniskelamin.capitalize(),
            'Umur': Numur,
            'Keluhan': Nkeluhan.capitalize(),
            'Tensi Darah': Ntensidarah,
            'Kategori Triage': '-'})
    print(f'\nNama Pasien terupdate')
    print(tabelpasien())

def delpasien():
    tabelpasien()
    Dpasien=input('Sebutkan nama yang hendak dihapus: ')
    pasien_ditemukan = False  # Inisialisasi variabel penanda

    for i, j in enumerate(pasien):
        if j['Nama'] == Dpasien.capitalize():
            del pasien[i]
            pasien_ditemukan = True  # Set penanda menjadi True
            print('\nPasien terupdate')
            tabelpasien()  # Cetak tabel setelah pembaruan

    if not pasien_ditemukan:  # Cek apakah pasien tidak ditemukan
        print('Nama pasien tidak ditemukan')

def kategoripasien() : #penambahan untuk kesalahan input
    age = int(input('berapa umur anda (tahun) : '))
    tdX = int(input('berapa tensi darah anda (mm) : '))
    tdY = int(input('berapa tensi darah anda (Hg): '))
    print(f'tensi darah anda {tdX}/{tdY} m0m/Hg')
    def tensi(age, tdX, tdY):
        if age<3: #tambah sama dengan
            if 40<tdX<90 or 60<tdY<65 :
                return 'normal'
            elif 90<tdX or 65<tdY :
                return 'tinggi'
            elif tdX<40 or tdY<60:
                return 'rendah'

        elif age<6:
            if 80<tdX<120 or 46<tdY<91 :
                return 'normal'
            elif 120<tdX or 91<tdY :
                return 'tinggi'
            elif tdX<80 or tdY<46:
                return 'rendah'

        elif 6<age<12:
            if 62<tdX<131 or 55<tdY<96 :
                return 'normal'
            elif 131<tdX or 96<tdY :
                return 'tinggi'
            elif tdX<62 or tdY<55:
                return 'rendah'

        elif 12<age<18:
            if 80<tdX<128 or 62<tdY<112 :
                return 'normal'
            elif 128<tdX or 112<tdY :
                return 'tinggi'
            elif tdX<80 or tdY<62:
                return 'rendah'

        elif age>18:
            if 90<tdX<120 or 60<tdY<80 :
                return 'normal'
            elif 120<tdX or 80<tdY :
                return 'tinggi'
            elif tdX<90 or tdY<60:
                return 'rendah'
            
    statustensi=tensi(age,tdX,tdY)
    print(f'tensi darah anda : {statustensi}')


    gjl=input('sebutkan gejalanya : ')
    def gejala(gjl):
        trM=['pernapasan berhenti','serangan jantung', 'stroke', 'kehilangan kesadaran','pendarahan', 'patah tulang', 'kecelakaan', 'kejang','gagal jantung', 'syok hemografi']
        trK=['patah tulang dalam', 'cedera punggung', 'luka parah tertutup', 'infeksi berat', 'nyeri dada', 'luka bakar', 'luka terbuka', 'kemungkinan patah tulang', 'asma akut']
        trH=['luka ringan', 'goresan', 'patah tulang', 'infeksi ringan', 'cedera ringan', 'kehamilan normal', 'batuk','pilek','maag akut', 'asma ringan']
        trHi=['bencana alam', 'tidak responsif', 'tidak sadar']
        if gjl.lower() in trM:
            return 'merah'
        elif gjl.lower() in trK:
            return 'kuning'
        elif gjl.lower() in trH:
            return 'hijau'
        elif gjl.lower() in trHi:
            return 'hitam'
        else:
            return 'Tolong masukan gejala yang similar'

    def maintriage():
        if gejala(gjl.lower()) == 'hijau' and tensi(age,tdX,tdY) == 'rendah':
            return 'kuning'
        elif gejala(gjl.lower()) == 'hijau' and tensi(age,tdX,tdY) == 'normal':
            return 'hijau'
        elif gejala(gjl.lower()) == 'hijau' and tensi(age,tdX,tdY) == 'tinggi':
            return 'hijau'
        elif gejala(gjl.lower()) == 'kuning' and tensi(age,tdX,tdY) == 'rendah':
            return 'merah'
        elif gejala(gjl.lower()) == 'kuning' and tensi(age,tdX,tdY) == 'normal':
            return 'kuning'
        elif gejala(gjl.lower()) == 'kuning' and tensi(age,tdX,tdY) == 'tinggi':
            return 'merah'
        elif gejala(gjl.lower()) == 'merah' and tensi(age,tdX,tdY) == 'tinggi':
            return 'merah'
        elif gejala(gjl.lower()) == 'merah' and tensi(age,tdX,tdY) == 'normal':
            return 'kuning'
        elif gejala(gjl.lower()) == 'merah' and tensi(age,tdX,tdY) == 'rendah':
            return 'merah'
        elif gejala(gjl.lower()) == 'merah' and tensi(age,tdX,tdY) == 'tinggi':
            return 'hitam'
        elif gejala(gjl.lower()) == 'hitam' and tensi(age,tdX,tdY) == 'normal':
            return 'hitam'
        elif gejala(gjl.lower()) == 'hitam' and tensi(age,tdX,tdY) == 'rendah':
            return 'hitam'

    triagestatus=maintriage()
    print(f'kategori triage adalah : {triagestatus} ')

def pembaruankondisi() :
    tabelpasien()
    Ppasien=input('Sebutkan nama yang hendak diperbarui: ')
    for i,j in enumerate(pasien): #i=index j=row
        if j['Nama']==Ppasien.capitalize(): #over indetation
            kondisi = input('\nKeluhan pasien terkini? ')
            pasien[i]['Keluhan'] = kondisi
            tensiD = input('\nTensi darah pasien terkini? ')
            pasien[i]['Tensi Darah'] = tensiD
            katTri = input('\nTriage pasien terkini? ')
            pasien[i]['Kategori Triage'] = katTri
            print('Data Pasien Terupdate')
            print(tabelpasien()) 
            break
        else :
            print('Nama pasien tidak ditemukan')

while True :
    opsi=input('''
        Selamat Datang di Puskemas Mugi Waras
        Pilih nomer yang hendak ditinjau:
        1. Daftar pasien saat ini
        2. Tambah pasien
        3. Hapus pasien
        4. Pengkategorian pasien
        5. Pembaharuan pasien
        6. Exit program
        
        Masukkan nomer yang hendak ditinjau : ''')

    if opsi == '1' :
        tabelpasien()
    elif opsi == '2':
         pasienbaru()
    elif opsi == '3':
         delpasien()
    elif opsi == '4':
         kategoripasien()
    elif opsi == '5':
         pembaruankondisi()
    elif opsi == '6':
        break
