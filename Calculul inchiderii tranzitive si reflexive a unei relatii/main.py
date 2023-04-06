#(De ex. pentru alfabetul {E,T,F,a,(,),+,-,*,/} relatia First (notata cu F) este
#F={(E,E), (E,T), (T,T), (T,F), (F,(), (F,a)} )
#Input: relatia (de ex. relatia F)
#Ouptut:inchiderea tranzitiva a relatiei (F+) si inchiderea tranzitiva si reflexiva a relatiei (F*)
def inchidere_tranzitiva(relatie):
    while True:
        nr=0
        for i in relatie:
            for j in relatie:
                if i==j:
                    continue
                else:
                    if i[1]==j[0]:
                        temp = [i[0],j[1]]
                        if temp in relatie:
                            continue
                        else:
                            relatie.append(temp)
                            nr+=1
                    elif i[0]==j[1]:
                        temp = [j[0],i[1]]
                        if temp in relatie:
                            continue
                        else:
                            relatie.append(temp)
                            nr+=1

        if nr==0:
            break

def inchidere_reflexiva(relatie,alfabet):
    for i in alfabet:
        if [i,i] in relatie:
            continue
        else:
            relatie.append([i,i])

alfabet = ["E","T","F","a","(",")","+","-","*","/"]
relatie = []
while True:
    i=input()
    if(i==""):
        break
    else:
        relatie.append([i.split(',')[0],i.split(',')[1]])
print("Inchiderea tranzitiva a relatiei: ")
inchidere_tranzitiva(relatie)
print(relatie)
print()
print("Inchiderea tranzitiva si reflexiva a relatiei: ")
inchidere_reflexiva(relatie,alfabet)
inchidere_tranzitiva(relatie)
print(relatie)
