import random
sc=0

while True:
    print("programma generatore di password")
    while True:
        N=int(input("inserisci il numero di password da generare"))
        if N<1 or N>50:
            print("N non può essere fuori dal range 1-50")
            continue
        else:
            break
    while True:
        L==int(input("inserisci lunghezza delle password"))
        if L<10 or L>20:
            print("L non può essere fuori dal range 10-20")
            continue
        else:
            break
    while True:
        print("\n1-password solo alfabetica")
        print("\n2-password solo alfanumerica")
        print("\n3-password alfabetica più caratteri speciali")

        if sc<1 or sc>3:
            continue
        else:
            break
    if sc==1:
        lista_caratt="ABCDEFabcdef"
    if sc==2:
        lista_caratt="ABCDEFabcdef123456"
    if sc==3:
        lista_caratt="ABCDEFabcdef12345@#&%$"
    
    nc=len(lista_caratt)

    for i in range(N):
        password=""
        for j in range(L):
            num=random.randint(0,nc)
            pasword=password+lista_caratt[num:num+1]
            print(str(i+1)+"\t"+password)
        continua=input("\nvuoi elaborare ancora? s/n")
        if continua=="n" or continua=="N":
            print("arrivederci")
            break
        

