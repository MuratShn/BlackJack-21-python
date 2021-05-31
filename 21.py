import random
import time

kartlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "kız", "joker", "papaz", "as"]


def kartcek():
    time.sleep(1)
    return random.choice(kartlar)


def oyun():
    farklı = ["joker", "papaz", "kız"]
    oyuncu = []
    kasa = []
    kasaKart = []
    kasaToplam = 0
    OyuncuToplam = 0
    kazan = True

    print("Kartlar dagıtılıyor...")
    time.sleep(1)

    kasa = [random.choice(kartlar), random.choice(kartlar)]
    oyuncu = [random.choice(kartlar), random.choice(kartlar)]
    while (kazan):
        for i in kasa:
            if(i == kasa[0]):
                continue
            kasaKart.append(i)
        print(f"Kasa: *,{kasa[1]} /// Oyuncu: {oyuncu}")

        istek = input("Kart İstermisiniz -> E/H :").upper()

        if(istek == "E"):
            print("Oyuncu kart çekiyor")
            oyuncu.append(kartcek())
            OyuncuToplam = 0
            for i in oyuncu:
                if(i in farklı):
                    i = 10
                    OyuncuToplam += i
                elif(i == "as" and OyuncuToplam <= 10):
                    i = 11
                    OyuncuToplam += i
                elif(i == "as" and OyuncuToplam > 11):
                    i = 1
                    OyuncuToplam += i
                else:
                    OyuncuToplam += i

            if(OyuncuToplam > 21):
                print(f"Kaybettiniz Oyuncu -> {oyuncu}")
                kazan = False

        if(istek == "H"):
            OyuncuToplam = 0
            for i in oyuncu:
                if(i in farklı):
                    i = 10
                    OyuncuToplam += i
                elif(i == "as" and OyuncuToplam <= 10):
                    i = 11
                    OyuncuToplam += i
                elif(i == "as" and OyuncuToplam > 11):
                    i = 1
                    OyuncuToplam += i
                else:
                    OyuncuToplam += i
            kasaToplam = 0
            for j in kasa:
                if(j in farklı):
                    j = 10
                    kasaToplam += j
                elif(j == "as" and kasaToplam <= 10):
                    j = 11
                    kasaToplam += j
                elif(j == "as" and kasaToplam > 11):
                    j = 1
                    kasaToplam += j
                else:
                    kasaToplam += j

            while kasaToplam < 16:
                print("Kasa Kart Çekiyor..")
                kasa.append(kartcek())
                print(f"Kasanın Kartları : {kasa}")

                kasaToplam = 0
                for j in kasa:
                    if(j in farklı):
                        j = 10
                        kasaToplam += j
                    elif(j == "as" and kasaToplam <= 10):
                        j = 11
                        kasaToplam += j
                    elif(j == "as" and kasaToplam > 11):
                        j = 1
                        kasaToplam += j
                    else:
                        kasaToplam += j

                if(kasaToplam > 21):
                    kazan = False
                    break

            if(kasaToplam > OyuncuToplam and kasaToplam <= 21):
                print(f""" 
                                KASA Kazandı
                    Kasa = {kasa} ///  Oyuncu = {oyuncu}
                      """)
                kazan = False
            elif(kasaToplam == OyuncuToplam and kasaToplam<=21):
                print(f""" 
                                 Berabere
                    Kasa = {kasa} ///  Oyuncu = {oyuncu}
                      
                      """)
                kazan = False
            else:
                print(f""" 
                                OYUNCU Kazandı
                    Kasa = {kasa} ///  Oyuncu = {oyuncu}
                      
                      """)
                kazan = False


def main():
    oyun()
    while input("\n\n\nDevam etmek için E tuşuna Basınız.....").upper() == "E":
        print("\n\n\n\n")
        oyun()


main()
