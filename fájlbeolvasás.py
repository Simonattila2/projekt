j=open("nevezetessegek.txt","r",encoding="utf-8")

adatok=[]

for i in j:
    t=i[:-1].split(";")
    adatok.append(t)

print(adatok)

def evszam(lista):
    kislista=[]
    for i in range(0,len(lista)):
        if lista[i][2]==kerdes1:
            cucc=lista[i][0]
            kislista.append(cucc)
            return kislista
    if kislista==None:
        print("Nincs ilyen")

def orszagnev(lista):
    kislista=[]
    for i in range(0,len(lista)):
        if lista[i][1]==kerdes2:
            cucc=lista[i][0]
            kislista.append(cucc)
            return kislista
    if kislista==None:
        print("Nincs ilyen")

def nevlista(lista):
    kislista=[]
    for i in range(0,len(lista)):
        kislista.append(lista[i][0])
    return kislista

def nevezetesseget(lista):
    kislista2=[]
    for i in range(0,len(lista)):
        if lista[i][0]==kerdes3:
            kislista2=lista[i][0]
            return kislista2
    if kislista2==None:
        print("Nincs ilyen")

valasztas=int(input("Írj be egy 1-est ha keresni akarsz évszám alapján. Írj be egy 2-est ha keresni akarsz országnév alapján. Írj egy 3-ast ha nevezetesség alapján akarsz keresni: "))

if valasztas==1:
    kerdes1=input("Adj meg egy évszámot: ")
    print(evszam(adatok))
elif valasztas==2:
    kerdes2=input("Adj meg egy országnevet: ")
    print(orszagnev(adatok))
elif valasztas==3:
    print(nevlista(adatok))
    input=("Írj be egy nevezetességet: ")
    print()
