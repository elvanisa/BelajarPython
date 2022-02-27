#conditions
#if else

"""
1. if = jika
2. kondisi
3. maka = aksi
"""
print("======INPUTAN=====")
gorengan = input("apakah kamu suka gorengan?")

if gorengan == "iya":
    print("wah sama aku juga suka gorengan")
else:
    print("kamu harus coba gorengan pak slamet")

print("======DEKLARASI=====")
a = 6

if a == 5:
    print("benar")
else:
    print("salah")

#ELIF ini adalah else if

nama = input("hai nama kamu sapa? ")

if nama == "elva": #kondisi 1
    print("hai elvaaaaa senang bertemu denganmu")
elif nama == "aulia": #kondisi 2
    print("hai aulia apa kabar?")
elif nama == "krissy": #kondisi 3
    print("halo krissy")
else:
    print("sapa lu gak kenal")