# Basit Hesap Makinesi


# Islemler
# Toplama
# Cikarma
# Carpma
# Bolme

# Programı baslattıgımızı varsayalım.

# =============================================================================
# a = input("Birinci sayiyi giriniz: ")
# b = input("ikinci sayiyi giriniz: ")
# =============================================================================

print("ISLEMLER")

print("Toplama icin -> 1")
print("Cikarma icin -> 2")
print("Carpma icin -> 3")
print("Bolme icin -> 4")

print("           ")
print("           ")

islem_numarasi = input("islem numarasi : ")

print("           ")
print("           ")

a = input("Birinci sayiyi giriniz: ")
b = input("ikinci sayiyi giriniz: ")

if int(islem_numarasi) == 1:
    print("Bu islemin sonucu : ",int(a) + int(b))


elif int(islem_numarasi) == 2:
    print("Bu islemin sonucu : ",int(a) - int(b))


elif int(islem_numarasi) == 3:

    print("Bu islemin sonucu : ",int(a) * int(b))

else:
    print("Bu islemin sonucu : ",int(a) / int(b))
