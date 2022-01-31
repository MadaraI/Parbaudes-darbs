# Blackjack skaitītājs
# Blekdžeka noteikumi ir ļoti vienkārši:
# spēlētāji ņem kārtis pa vienai, cenšoties savākt vairāk punktu nekā pretiniekiem, bet ne vairāk kā 21.

# Kavā ir visas kārtis no 2 līdz 10 ieskaitot, tās tiek skaitītas pēc to vērtības, 
# karaļi (K), dāmas (Q) un kalpi (J), katrs 10 punktu vērts, kā arī dūži (A), kas var tikt skaitīti kā 1 vai 11 punkti, atkarībā, kā labāk. 

# Programmas ievadē raksta visas attiecīgā gājiena kārtis, atdalot ar atstarpi:
# skaitļi 2–9 ar to vērtībām, 10 kā T
# J, Q, K – kalps, dāma, karalis
# A – dūzis

# Programmas izvadē parāda punktus, ja tie ir ne vairāk kā 21, vai vārdu "Bust", ja tie ir vairāk kā 21, t.i. spēlētājs nekavējoties zaudē.
# Izveido un komentāros uzraksti nepieciešamo skaitu ievades–izvades pārus, lai pārbaudītu pēc iespējas dažādākus gadījumus.

vertibas = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

def punkti(gajiens):
    gajienaSumma = 0
    for katrs in gajiens:
        gajienaSumma += vertibas[katrs]
    
    for katrs in gajiens:
        if katrs == "A":
            if gajienaSumma <= 21:
                break
            else:
                gajienaSumma -= 10
    
    if gajienaSumma <= 21: 
        print(gajienaSumma)
    else:
        print("Bust")

gajiens = [karts for karts in input("Ievadi gājiena kārtis, atdalot tās ar atstarpi:").split()]
punkti(gajiens)

#(5 7 8 T) - Bust
#(A 5 6 2 2 Q)- Bust
#(2 5 3) - 10
#(0 A 5 7 8 ) - Kļūda
#(A A A A) - 14
#(2 2 2 2 3 3 3) - 17
#(A Q T T) - Bust
#(11 5 7) - Kļūda