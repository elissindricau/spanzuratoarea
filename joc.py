"""
sa apara un cuvant ascuns si fiecare litera sa apara codata printr-o linie
cand utilizatorul introduce o litera
    daca litera se afla in cuvant, reafisam cuvantul cu litera respectiva de oricate ori apare cuvantu
        daca s-a ghicit si ultima litera, se afiseaza un mesaj de final
    daca nu se gaseste litera, se afiseaza cate sanse mai are jucatorul
        daca nu mai are sanse, se afiseaza un mesaj de pierdere
optional: afisam omuletul
"""
import random

lista_cuvinte = ['caine', 'girafa', 'lalea', 'lup', 'pisica', 'elefant', 'castor', 'maimuta', 'delfin', "cal", "capra"]


nr_vieti = 6

spanzuratoare = [
"     ________",
"     |      |",
"            |",
"            |",
"            |",
"         ___|___"
]

lista_linii = [
    (0, 0, "0"),
    (2, 5, "O"),
    (3, 4, "/"),
    (3, 5, "|"),
    (3, 6, "\\"),
    (4, 4, "/"),
    (4, 6, "\\")
]

def adauga_membru(lista_linii, sansa, spanzuratoare):
    membru = nr_vieti - sansa
    if membru == 0:
        return spanzuratoare
    else:
        linia, randul, valoarea = lista_linii[membru]
        linia_noua = schimba_chr(randul, valoarea, spanzuratoare[linia])
        spanzuratoare[linia] = linia_noua
        return spanzuratoare




def afisare_spanzuratoare(spanzuratoare):
    for linie in spanzuratoare:
        print(linie)



def schimba_chr(index, chr, cuvant):
     cuvant = cuvant[:index] + chr + cuvant[index+1:]
     return cuvant



def afisare_cuvant(cuv):
    sir = ""
    for i in range(len(cuv)):
        sir = sir + cuv[i] + " "
    print(sir)

def joc():
    print("Bine ai venit in jocul Spanzuratoarea!")
    print("by Eliss Indricau")
    raspuns = "da"
    while raspuns == "da":
        raspuns = "nu"
        cuvant = random.choice(lista_cuvinte)
        cuvant_linii = genereaza_linii(cuvant)
        spanzuratoarea(cuvant, cuvant_linii)
        raspuns = input("Vrei sa mai joci? (da/nu): ")


def spanzuratoarea(cuvant, sir):
    jocul_continua = True
    sanse = nr_vieti
    spanzuratoare_noua = spanzuratoare
    while jocul_continua:
        print("Mai ai {} sanse".format(sanse))
        afisare_spanzuratoare(spanzuratoare_noua)
        afisare_cuvant(sir)
        litera = input("Scrie o litera: ")
        litera_gasita = False
        for i in range(len(cuvant)):
            if cuvant[i] == litera:
                litera_gasita = True
                sir = schimba_chr(i, litera, sir)
                #print(sir)
        if not litera_gasita:
            sanse -= 1
            spanzuratoare_noua = adauga_membru(lista_linii, sanse, spanzuratoare_noua)
        if sanse == 0:
            jocul_continua = False
            afisare_spanzuratoare(spanzuratoare_noua)
            print("Ai pierdut!")
            print("Cuvantul tau a fost: ")
            afisare_cuvant(cuvant)
        if sir == cuvant:
            jocul_continua = False
            print("Ai castigat!")
            print("Cuvantul tau este: ")
            afisare_cuvant(cuvant)



def genereaza_linii(cuvant):
    sir = ""
    for i in range(len(cuvant)):
        sir = sir + "_"
    return sir


joc()
