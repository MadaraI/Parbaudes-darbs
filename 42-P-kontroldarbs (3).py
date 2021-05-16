import os # modulis, kurš māk operētājsistēmas termināļa komandas.
import json # tiek importēts json modulis

if not os.path.exists('pasutijumi.json'): # sākas datu ievade
    print("Faila nav. Neko darīt, taisīšu tukšu") # Tiek izveidots json tukšs fails
    masivs = []
    dati = json.dumps(masivs) #sagatavo ierakstīšanai teksta failā
    with open('pasutijumi.json', 'w', encoding='utf-8') as f: # Atveram failu un datus ieraksta
        f.write(dati)
with open("pasutijumi.json", "r", encoding='utf-8') as fails: #Ierakstītos datus nolasa
    dati = fails.read()
masivs = json.loads(dati) # beidzas datu izvade



def informacija(): # tiek uztaisīta funkcija un sākas datu ievade (klients tiek iepazīstināts ar pasūtījuma informāciju)
    nosacijumi = "Iepazīsties ar pasūtījuma nosacījumiem"
    teksts = "Apdruka ar tekstu 5 EUR"
    zime = "Apdruka ar vienkrāsainu zīmi 7 EUR"
    fotografija = "Apdruka ar fotogrāfiju 20 EUR"
    piegade = "Pasūtījuma piegāde 7 EUR"
    atlaide = "Pasūtījuma summai pārsniedzot 100 EUR, tiek piemērota 5% atlaide"
    print(nosacijumi)
    print(teksts)
    print(zime)
    print(fotografija)
    print(piegade)
    print(atlaide)
informacija() # beidzas datu ievade

def izvelne(): # tiek izveido jauna funkcija un sāks datu ievade (klientam ir iespēja izvēlēties, ko viņš vēlas darīt)
    print("Izvēlies ko darīsi")
    print("1: reģistrēt jaunu pasūtījumu")
    print("2: meklēt pasūtījumu pēc apdrukas veida")
    print("3: beigt pasūtījuma noformēšanu")
    izv = input("Ko izvēlējies? ")
    if izv == "1":
        apdruka1()
    elif izv == "2":
        mekle()
    elif izv == "3":
        beigas()
    else:
        print()
        izvelne() # beidzas datu ievade

def summa(skaitlis, cena, piegade): # sākums jaunai funkcijai, sākas datu ievade (tiek aprēķināta pasūtījuma summa ar vai bez piegādes)
    tkreklu_summa = skaitlis*cena
    if piegade == False:
        if tkreklu_summa > 100:
            tkreklu_summa1 = tkreklu_summa - (tkreklu_summa * 5 / 100)
            print (f"{tkreklu_summa1:.2f} EUR")
        else:
            print (f"{tkreklu_summa:.2f} EUR")
    elif piegade == True and tkreklu_summa > 100:
        summa1 = tkreklu_summa*5/100
        summa3 = tkreklu_summa-summa1 + 7
        print(f"{summa3:.2f} EUR")
    elif piegade == True and tkreklu_summa < 100:
        pasutijuma_summa = tkreklu_summa + 7
        print(f"{pasutijuma_summa:.2f} EUR")
    else:
        pass # beidzas šīs funkcijas datu ievade

def apdruka1(): # jauna funkcija un sākas datu ievade (klientam tiek uzdoti jautājumi par viņa pasūtījumu)
    skaitlis = int(input("Ievadiet kreklu skaitu"))
    apdruka = input("Vai jūs vēlaties tekstu, zīmi vai fotogrāfiju uz krekla?")
    if apdruka == "teksts":
        cena = 5
        teksts = input("Kādu tekstu vēlaties?")
        krasa = input("Kādā krāsā vēlaties tekstu?")
    elif apdruka == "zīme":
        cena = 7
        krasa1 = input("Kādā krāsā vēlaties zīmi?")
        links = input("Vai vēlaties pievienot linku, kā piemēru, ko liksiet uz krekla?")
        if links == "jā":
           links1 = input("Ievadiet linku")
        else:
            pass
    elif apdruka == "fotogrāfija":
        cena = 20
        links2 = input("Ievadiet linku, kā piemēru, ko liksiet uz krekla")
    else:
        pass

    piegade1 = input("Vai jums ir nepieciešama piegāde?")
    if piegade1 == "jā":
        piegade = True
        adrese = input("Ievadiet, lūdzu, adresi")
    else:
        piegade = False
    summa(skaitlis, cena, piegade)
    
    
    if apdruka == "teksts":
        var_teksts = {} # tiek uztaisīta jauna vārdsnīca, kurā rakstīs pasūtījumu
        var_teksts["apdruka"] = apdruka
        var_teksts["cena"] = cena
        var_teksts["teksts"] = teksts
        var_teksts["krasa"] = krasa
        masivs.append(var_teksts) # pasūtījuma vārdnīca tiek ierakstīta masīvā
        print(masivs)
    elif apdruka == "zīme":
        var_zime = {}
        var_zime["apdruka"] = apdruka
        var_zime["cena"] = cena
        var_zime["krasa1"] = krasa1
        if links == "jā":
            var_zime["links"] = links
            var_zime["links1"] = links1
        else:
            var_zime["links"] = links
        masivs.append(var_zime) 
    elif apdruka == "fotogrāfija":
        var_foto = {}
        var_foto["apdruka"] = apdruka
        var_foto["cena"] = cena
        var_foto["links2"] = links2
        masivs.append(var_foto)
        

    for z in masivs:
        for i in z:
            print(f"{i}: {z[i]}")
        print()

    dati = json.dumps(masivs, ensure_ascii=False)
    with open("pasutijumi.json", "w", encoding='utf-8') as fails:
        fails.write(dati)
    izvelne() # beidzas visgarākā funkcija darbā 


def mekle(): # jauna funkcija, sākas koda ievade
    with open("pasutijumi.json", "r", encoding='utf-8') as fails:
        dati = fails.read()
    masivs = json.loads(dati)  # nolasīto teksta failu parvērš vārdnīcu masīvā.
    koMeklet = input('Kādu vērtību pārbaudīt?') 
    atrada = False 
    for z in masivs:
        if koMeklet in z["apdruka"]: # meklē pēc vērtības apdruka
            print(f'Atrasts:')
            atrada = True 
            for atslega in z: 
                print(f'{atslega}: {z[atslega]}') 
    if not atrada:
        print("Nekas nav atrasts\n")
    izvelne() # funkcija beidz savu datu ievadi


def beigas(): # tiek izveidota pēdējā funkcija un sākas datu ievade
    dati = json.dumps(masivs, ensure_ascii=False)
    with open("pasutijumi.json", "w", encoding='utf-8') as fails: # masīvs ar vārdnīcām tiek ierakstīti json failā
        fails.write(dati)
    print("Jūsu pasūtījums tiks noformēts tuvāko dienu laikā. Uz tikšanos!")
izvelne() # beidzas datu ievade, un darbs ir gatavs