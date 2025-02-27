gameOn = True
rooms = [] # Hol jártunk eddig?
contents = [] # A szobák tartalma ahol már jártunk
health = 3
solution = "4686"
lámpák = "0000000" # 7 db 0

print("""
Üdvözöllek a szabadulószobában!
14 ajtó van előtted, ebből 13 mögött egy feladványban, egy pedig a
külvilághoz vezető utat rejti.
""")
while gameOn:
    room_number = int(input("Add meg a szobaszámot (0-13) [-1]!\n"))
    if room_number == -1:
        print("Eddig ezeket találtad:")
        for i in range(len(rooms)):
            print(f"{rooms[i]}. szoba - {contents[i]}")
    elif room_number == 0:
        if room_number not in rooms:
            print("Ebben a szobában nincs semmi, csak egy villanykörte ami világít, de feldűhít, hogy nem találsz itt semmit, ezért mérgedben összetöröd a villanykörtét. Teljeses a sötétség, de úgy döntessz, hogy elkezdessz a sötétben tapogatózni. Eme Darwin díjas tetted miatt megvágod a szilánkokkal a kezed, de matatás közben találsz egy kulcsot.")
            rooms.append(room_number)
            contents.append("kulcs")
            if "lezárt doboz" in contents:
                print("Előveszed a lezárt dobozt a táskádból és megpróbálod kinyitni a kulccsal. Azt tapasztalod, hogy egy szelet hús van benne.")
                contents.append("hús")
                rooms.append(room_number)
        else:
            print("A kulcsot elraktad, mást már nem tudsz itt csinálni.")
    elif room_number == 1:
        if room_number not in rooms:
            print("A szobában egy kisebb festményt találsz. Elrakod.")
            contents.append("festmény")
            rooms.append(room_number)
        else:
            print("Ez a szoba már üres.")
    elif room_number == 2:
        if room_number not in rooms:
            print("A szobába lépve számokat látsz a falon: 1010011")
            rooms.append(room_number)
            contents.append("1010011")
        else:
            print("Még mindig ugyan azokat a számokat látod a falon: 1010011")    
    elif room_number == 3:
        if room_number not in rooms:
            print("A szobában néhány macskát találsz akik egy tálból falatoznak. Miután jobban megvizsgálod a szobát azt tapasztalod, hogy a táljukra egy 2-es számjegy van felírva.")
            rooms.append(room_number)
            contents.append("Cicák esznek egy 2-es tálból")
        else:
            print("A cicák még mindig a 2-es számjegyes tálból esznek.")    
    elif room_number == 4:
        if room_number not in rooms:
            rooms.append(room_number)
            contents.append("Egy tábla tele villanykörtékkel")
        if lámpák == "1010011":
            print("A táblán kirajzolódik egy 6-os számjegy")
            rooms.append(room_number)
            contents.append("6-os számjegy")
        else:
            print("A szobában egy táblát látsz tele villanykörtével, de kapcsoló sehol.")
    elif room_number == 5:
        if room_number not in rooms:
            print("Egy egyenlet van a falon: x = 10111 - 10001")
            rooms.append(room_number)
            contents.append("x = 10111 - 10001")
        else:
            print("Továbbra is csak az egyenlet van a falon: x = 10111 - 10001")
    elif room_number == 6:
        if room_number not in rooms:
            rooms.append(room_number)
            contents.append("oroszlán")
        print("Ebben a szobában egy éhes oroszlánt találsz, látod, hogy van valami mögötte a falon, de nem tudod elolvasni...")
        akció = input("Megpróbálod elcsalni az oroszlánt, hogy lásd mi van a falon? (igen/nem)\n")
        if akció == "igen":
            if "hús" in contents:
                print("Odadobod az oroszlánnak a húst és meglátsz a falon egy 4-es számot.")
                rooms.append(room_number)
                contents.append("4-es szám a falon")
            else:
                print("Felfalt téged az oroszlán.")
                gameOn = False
        else:
            print("Elhagyod a szobát. Majd későbbb visszajössz")
    elif room_number == 7:
        if room_number not in rooms:
            print("Ezen ajtó mögött egy rozsdás baltát találsz. Zsebre vágod.")
            rooms.append(room_number)
            contents.append("balta")
        else:
            print("Ez most már csak egy üres szoba...")
    elif room_number == 8:
        if room_number not in rooms:
            print("Belépsz a szobába és egy nagyon fura képet találsz, van rajta 2 bohóc, akik egy épületre másnak amin van egy kérdőjel és közben két majom dobálgatja őket fagyitortával. Ja, és ezt az egészet végignézi egy macska...")
            rooms.append(room_number)
            contents.append("Festmény 2 bohócról, 2 majomról meg egy cicáról")
        else:
            print("Ez már megint ez a fura bohócos cicás kép...")
    elif room_number == 9:
        if room_number not in rooms:
            print("Egy cetlit találsz a szobában, amire az van írva, hogy válts át binárrisból decimálisba. Ez lehet, hogy egy nyom egy másik szobához...")
            rooms.append(room_number)
            contents.append("papír cetli: bináris -> decimális")
        else:
            print("Ez a szoba már üres.")
    elif room_number == 10:
        print("Ebben a szobában találhatü a szabadsághoz vezető út, de az ajtaja le van zárva egy számkombinációs lakattal. Ezek a számok el vannak rejtve valahol a többi szobában. Csak 3 próbálkozásod van kitalálni, úgyhogy óvatosan tippelj!")
        if room_number not in rooms:
            rooms.append(room_number)
            contents.append("kijárat")
        válasz = input("Megpróbálod kinyitni a zárat? (igen/nem)\n")
        if válasz == "igen":
            tipp = input("Add meg a 4 számjegyet!\n")
            if tipp == solution:
                gameOn = False
                print("Gratulálok! Sikeresen kijutottál a szabadulószobából!")
            else:
                print("Nem ez a helyes számkombináció.")
                health -= 1
                print(health, "próbálkozásod maradt.")
                if health == 0:
                    gameOn = False
                    print("Ez volt az utolsó lehetőséged, és nem találtad el. Az ajtó örökre eltűnt, mostmár itt maradsz a majmokkkal, macskákkal és az oroszlánnal mindörökké.")
        else:
            print("Majd később visszajössz.")
    elif room_number == 11:
        if room_number not in rooms:
            print("A szobában egy ketrec van, amiben egy majom ül és unatkozik")
            rooms.append(room_number)
            contents.append("1 majom")
        else:
            print("Még mindig itt a majom.")   
    elif room_number == 12:
        if room_number not in rooms:
            rooms.append(room_number)
            contents.append("7 kapcsoló a falon")
        print("7 kapcsolót látsz a falon.")
        print("Fel vagy le tudod kapcsolni őket úgy, hogy beírsz egy 1-esekből és 0-kból álló 7 jegyű számot.")
        print("Az 1-es felkapcsolja, a 0 lekapcsolja.")
        lámpák = input("Add meg a 7 számjegyet (pl.: 0011101)")
    elif room_number == 13:
        if room_number not in rooms:
            rooms.append(room_number)
            contents.append("faláda")
        print("A szobában egy sérült faládát talász, a réseken keresztül látod, hogy van valami a ládában.")
        if "balta" in contents:
            print("A talált baltáddal szétvered a ládát, és egy kisebb lezárt dobozt találsz benne.")
            contents.append("lezárt doboz")
            rooms.append(room_number)
            if "kulcs" in contents:
                print("A korábban talált kulccsal kinyitod a dobozt, és egy szelet húst találsz benne.")
                contents.append("hús")
                rooms.append(room_number)
        else:
            print("Talán valami eszközzel, szét tudnád verni a ládát...")

        
