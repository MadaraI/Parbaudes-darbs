# Programmatūra balsošanas rezultātu analīzei

# Atkarībā no rezultātiem, balsojumus var iedalīt šādi:
# kvalificēts vairākums: PAR ir vairak kā 2/3 balsu
# absolūts vairākums: PAR ir vairāk nekā puse no teorētiska dalībnieku skaita
# vienkāršs vairākums: balso vairāk kā puse dalībnieku un PAR ir vairāk nekā PRET vai ATTURAS

# Funkcijā balsojums jāievada četri lielumi, visi ir veseli skaitļi:
# dalibnieki: cik personas ir organizācijā (nevis cik atnāca balsot, bet vispār,
# piemēram, Saeimā ir 100. Reizēm, kāds nepiedalās, jo strīmo facebookā blēņas, bet šā vai tā kopā ir 100)
# Par, pret , atturas – attiecīgi balsojošo skaits

# Programma pilna kļūdu. Atrod kļūdas, ja iespējams, nosauc to veidus un izlabo tās!

def balsojums(dalibnieki, par, pret, atturas): # Sintakses kļūda. funkcijai tika izmantotas nepareizās iekavas, kā arī lai atdalītu lielumus, kas tiek ierakstīti funkcijā, ir jāatdala ar komatu.
    kopaBalsotaji = par + pret + atturas
    if kopaBalsotaji > dalibnieki: #Loģikas kļūda? Vienmēr sākas ar if, else izmanto beigās
        print("Te kaut kas nav kārtībā")
    else:
        if kopaBalsotaji > dalibnieki // 2 and (par > pret and par > atturas):
            print("Vienkāršs vairākums") #Sintakses kļūda. Jāizmanto pēdiņas.  ' '  ir vienkārši kā komentārs, bet ne īsti kā komentārs
        elif par < kopaBalsotaji > 2 // 3: #Sintakses kļūda
            print("Kvalificēts vairākums")
        elif par > dalibnieki // 2:
            print("Absolūts vairākums")

        elif par // dalibnieki ==  0: #Loģikas vai sitnakses kļūda? dalīt ar nulli nevar
            print("Nav vairākuma")

balsojums(88, 22, 22, 0) # lai pārbaudītu programmu, šos lielumus jāmaina

# balsojums(100, 42, 59, 10) te kaut kas nav kārtībā
# balsojums(100, 88, 4, 5) vienkāršs vairākums
# balsojums(100, 40, 32, 8) vienkāršs vairākums (man liekas, ka es kaut ko neesmu pareizi izdarījusi)
#es vairs neko nesaprotu
#balsojums (100, 28, 25, 44) kvalificēts vairākums
#balsojums (88, 22, 22, 0) kvalificēts vairākums
#es 100% kaut ko izdarīju nepareizi

