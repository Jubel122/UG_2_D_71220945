print ("===MAKANAN===")

def jenismakanan():
    global totalmkn
    global pesanan
    global mkn
    print ("1.telur bakar - Rp 70000")
    print ("2. lele terbang mas bhe - Rp 10000")
    print ("3. es coklat lempu - Rp 5000")
    print ("4. es doger langensari - Rp 13000")
    nomor = int(input("masukkan pilihan"))
    pesanan = int(input("jumlah pesanan"))

    if nomor ==1:
        hargamakanan=pesanan*7000
        print(pesanan,"pesanan telur bakar = Rp",totalmkn)
        pesanan=("telur bakar")
    elif nomor==2:
        hargamakanan=pesanan*10000
        print(pesanan,"lele terbang mas bhe = Rp", totalmkn)
        pesanan=("lele terbang mas bhe")

    elif nomor==3:
        hargamakanan=pesanan*5000
        print(pesanan,"es doger lempu = Rp", totalmkn)
        pesanan=("es doger lempu")

    elif nomor==4:
        hargamakanan=pesanan*13000
        print(pesanan,"es doger langensari = Rp", totalmkn)
        pesanan=("es doger langensari")
    

    

jenismakanan()

# print("\nTotal harus Dibayar: Rp",total pesanan)

