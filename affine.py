import pyfiglet



print(pyfiglet.figlet_format("Affine Cipher\n"))
print(pyfiglet.figlet_format("Eray Atalay\n", font = "small"))

alfabe = "abcdefghijklmnopqrstuvwxyz"
print("Encryption : 1\n")
print("Decryption : 2\n")
islem = int(input("Yapmak istediğiniz işlemi seçiniz: "))

if islem == 1:

    a = int(input("a değerini giriniz a: "))
    b = int(input("b değerini giriniz b: "))
    plaintext = input("Plaintext'i giriniz: ").lower()

    sira_listesi = []
    
    for harf in plaintext:
        if harf == " ":
            continue
        elif harf in alfabe:
            sira_listesi.append(alfabe.index(harf))
        else:
            print("Geçersiz karakter:", harf)
            exit()

    islemli_liste = [(x * a + b)%26 for x in sira_listesi]

    ciphertext = [alfabe[num] for num in islemli_liste]

    print("Ciphertext:", "".join(ciphertext))

elif islem == 2:

    a = int(input("a değerini giriniz a: "))
    b = int(input("b değerini giriniz b: "))
    ciphertext = input("Ciphertext'i giriniz: ").lower()

    sira_listesi = []
    a_inv = pow(a, -1, 26)

    for harf in ciphertext:
        if harf == " ":
            continue
        elif harf in alfabe:
            sira_listesi.append(alfabe.index(harf))
        else:
            print("Geçersiz karakter:", harf)
            exit()

    islemli_liste = [((y - b) * a_inv) % 26 for y in sira_listesi]

    plaintext = [alfabe[num] for num in islemli_liste]

    print("Plaintext:", "".join(plaintext))

else:
    print("Geçersiz işlem seçimi.")