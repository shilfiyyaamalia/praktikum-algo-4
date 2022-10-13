"""
Created on Thu Oct 13 20:45:07 2022

@author: shilaaaa
"""

import calendar
print("Program dapat menentukan jumlah hari di salah satu bulan")
ulang = "cc"
while ulang == "cc" or ulang == "ss": 
    year = int(input("Masukan Tahun yang anda inginkan: ")) 
    month = int(input("Masukan Bulan yang anda inginkan: "))
    print("Ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke",month)
    ulang = input("ketik'cc' jika ingin lanjut, ketik 'ss' jika stop ")
    if ulang == "ss":
        print("Terimakasih sudah Menggunakan program ini")
        print("shilfiyya amalia asdi 065002200032")
        break