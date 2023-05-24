import random
punkti = 0
apjoms = 0 

 

skaits = int(input("Cik uzdevumu vēlies risināt"))


print("Cik lielu apjomu vēlies risināt  ? ievadi 1 ja no 0 - 9 , ievadi 2 ja no 0 -20 , ievadi ja no 0 -30")
apjoms=int(input("ievadi 1 vai 2 vai 3:"))


if apjoms == 1:
    apjoms= 9
if apjoms == 2:
    apjoms =20
if apjoms == 3:
    apjoms= 30







for i in range(skaits):
    a = random.randrange(0,apjoms)
    b = random.randrange(0,apjoms)
    
    print("Cik ir ", a , "*", b , "=")
    atb = int(input("Atbilde :"))

    if a * b == atb:
        print("PAREIZI")
    else:
        print("NEPAREIZI. Pareizā atbilde ir:", a*b)



for i in range(skaits):
    a = random.randrange(0,apjoms)
    b = random.randrange(0,apjoms)


print("Cik ir ", a , "+", b , "=")
atb = int(input("Atbilde :"))

if a + b == atb:
        print("PAREIZI")
        punkti =+1
else:
        print("NEPAREIZI. Pareizā atbilde ir:", a+b)







for i in range(skaits):
    a = random.randrange(0,apjoms)
    b = random.randrange(0,apjoms)

print("Cik ir ", a , "-", b , "=")
atb = int(input("Atbilde :"))

if a - b == atb:
        print("PAREIZI")
        punkti =+1
else:
        print("NEPAREIZI. Pareizā atbilde ir:", a-b)







for i in range(skaits):
    a = random.randrange(0,apjoms)
    b = random.randrange(0,apjoms)

print("Cik ir ", a , "/", b , "=")
atb = int(input("Atbilde :"))

if a * b == atb:
        print("PAREIZI")
        punkti =+1
else:
        print("NEPAREIZI. Pareizā atbilde ir:", a/b)




