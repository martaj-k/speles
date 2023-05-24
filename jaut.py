jautajumi = ("Kad Latvija iestājās Eiropas Savienībā?  ;",
             "Desmitais Latviešu alfabēta burts ? ;",
             "Putns , kas spēj lidot visos virzienos? ;",
             "Ar cik valstīm Latvijai ir sauszemes robeža? ;",
             "Kura ir lielākā saldūdens zivs? ;")

varianti = (("A.  2003", "B.  2001", "C.  2004", "D.  2008"  ),
            ("A.  g", "B.  m", "C.  k", "D.  p"),
            ("A.  Kalibri", "B.  Gārnis", "C.  Sarkanais kardinālis", "D.  Kolibri"),
            ("A.  4", "B.  3", "C.  5", "D.  2"),
            ("A.  Līdaka ", "B.  Sams", "C.  Līnis", "D.  Renģe") )


atbildes = ("C","A","D","A","B")
min = []
punkti = 0
jautaj_num = 0
 



for i in jautajumi:
    print("----------------------------------------")
    print (i)
    for var in varianti[jautaj_num]:
        print(var)




    ieraksts = input("Ievadi atbildes variantu (A, B, C , D):").upper()
    # upper no w3 school(automātiski mazos burtus pieraksta par lielajiem)
    min.append(ieraksts)
    if ieraksts == atbildes[jautaj_num]:
        punkti += 1 
        print("PAREIZI")
    else:
        print("NEPAREIZI")
    
    jautaj_num += 1


print ("---------------------------")
print("REZULTĀTI")

print("pareizās atbildes : C ,D ,A ,B")

punkti = int(punkti / len(jautajumi) * 100)




print (f"Tavs rezultāts ir: {punkti} %")
