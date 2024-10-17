print('selamat datang di penyewaan bus irfan')
print('====================================================================')
nama= input(          'masukan nama anda                      :')
plat= input(          'plat nomer kendaraan bus               :')
barang_dibawa= input( 'barang yang di bawa                    :')
barang_x_dibawa=['sajam','senjata api','minuman keras']
usia_rata=int(input(  'masuka usia rata-rata                  :'))
jumlah=int(input(     'masukan jumlah penumpang               :'))
perjam=int(input(     'perorang 1 jam 5000, mau berapa jam    :'))
perorang=5000
total=(jumlah * perorang * perjam)
print(total)
jenis_ewallet=['dana', 'ovo', 'gopay', 'mbanking']
print(jenis_ewallet)
ewallet= input(       'masukan jenis pembayaran               :')
bayar=int(input(      'masukan jumlah pembayaran anda         :'))
ticket=True
print(ticket)
hasil=('selamat pesanan anda berhasil' if bayar==total and 
       ticket==True and ewallet in jenis_ewallet and barang_dibawa not in 
       barang_x_dibawa and usia_rata<50 else 'maaf pesanan anda gagal')
print(hasil)
print('====================================================================')
