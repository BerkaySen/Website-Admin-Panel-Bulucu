#!/usr/bin/env python3
# 'utf-8'
import httplib2
import socket
import os
import http
import sys
Banner = """
*-------------------------------------------------------*
|                                                       |
|       Çok Fonksiyonlu Admin Panel Bulucu              |
|                                                       |
|                                                       |
*-------------------------------------------------------*\n

"""
Yardım = """"
    ***** Yardım Menüsüne Hoşgeldiniz *****
programımızı kullanmak için admin paneli taranacak web sitenizi http://www.google.com
Şeklinde yazabilirsiniz.
Admin Panel Seçeneklerini daha da arttırmak için yeni eklenecek verileri eklenecek.txt nin içerisine 
koyup kaydediniz.Daha sonra programımıza ekle yazıp enterlayınız programımız sizin için yeni
admin panel seçeneklerini admin_liste.txt içerisine yükleyecektir.
Yüklerken de Asla aynı seçeneği ikinci defa yüklemeyecektir. Bu şekilde aynı admin paneli birden fazla
kez taramayacağı için zamandan da kazanacaksınız.
"""




url_txt = open("admin_liste.txt","r")
print(Banner)
url_giris = input("Yardım için yardım Giriniz\nLütfen bir url giriniz Örnek(www.google.com) : ")

if(url_giris == "yardım"):
    print(Yardım)
    
elif(url_giris=="ekle"):
    import ayrıstirici
    url_txt.close()


else:
    os.system("whois "+"www.google.com")
    http = httplib2.Http()
    url_txt.close()

    def txtuzunluk():
        url_txt11 = open("admin_liste.txt", "r")
        i = 0
        while True:
            i += 1
            if url_txt11.readline() == "":
                break
        url_txt11.close()
        print(i)
        return i


    for i in range(txtuzunluk() - 1):
        admin = url_txt.readline()
        url_top = url_giris + "/" + admin
        try:
            bag = http.request(url_top)[0]
            if (bag.status == 200):
                print("\033[1;31;10m[ + ]" + "  [ " + str(bag.status) + " ] " + url_top)

            elif (bag.status == 404):
                print("\033[1;32;10m[ - ]" + "  [ " + str(bag.status) + " ] " + url_top)
            else:
                print("\033[1;32;10m[ - ]" + "  [ " + str(bag.status) + " ] " + url_top)
        except httplib2.ServerNotFoundError or socket.gaierror:
            print("Böyle Bir Site Bulunamadı ... Veya Yanlış url girdiniz ...")
            break

