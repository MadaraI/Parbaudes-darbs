# Programma pārvērš ievadītos vārdus pupiņvalodā un pa vienam parāda sākotnējo un pārveidoto vārdu
# Vārdi ievades brīdī tiek ierakstīti masīvā

# Ar atkļūdotāju noteikt šādu mainīgo vērtības (atbildes raksti tepat sagatavotajās rindās):
# patskaniLieli: 'AĀEĒIĪOUŪ'
# vardi ['sudrabs', 'koks', 'māja']
# datu tips mainīgajam burts: list??

## nākamjaiem diviem padomā un eksperimentē, kā uzrakstīt vārdu, lai atbildes atšķirtos
# viensVards pirms rindas "viensVards = viensVards.title()" nostrādāšanas:auto
# viensVards pēc rindas "viensVards = viensVards.title()" nostrādāšanas:Apauputopo (es īsti nesapratu šo uzdevumu)


patskani = "aāeēiīouū"
patskaniLieli = patskani.upper()
visiPatskani = patskani+patskaniLieli
def pupinas(vardi):
    for viensVards in vardi:
        sakotnejaisVards = viensVards    
        for burts in visiPatskani:
            viensVards = viensVards.replace(burts, burts+"p"+burts)
        viensVards = viensVards.title()
        print(sakotnejaisVards, viensVards)

vardi = [vards for vards in input("Raksti vārdus, atdalot tos ar atstarpi:").split()]
pupinas(vardi)