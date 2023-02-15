masukkanbrand = (input("masukkan nama brand"))
hargabrand = (input("masukkan harga brand"))


total_belanja = int(input('Total Belanja: Rp.'))
 
if (total_belanja >= 10000000) and (total_belanja < 10000000):
  harga_akhir = total_belanja - (0.1*total_belanja)
  print(', anda mendapat diskon 10%')
elif (total_belanja >= 25000000) and (total_belanja >25000000):
  harga_akhir = total_belanja - (0.25*total_belanja)
  print('Selamat, anda mendapat diskon 2%')

else:
  harga_akhir = total_belanja
   
print('total uang yang harus anda bayarkan adalah: Rp.',round(harga_akhir,2))


total_belanja = int(input('Total Belanja: Rp.'))
