import copy

def reguli_simplificare(expresie):
    e1 = expresie.split("(")
    e2 =[]
    for i in e1:
        e2.append(i.replace(")",""))
    for i in e2:
        if i=="":
            e2.remove(i)
    for i in e2:
        if i=="":
            e2.remove(i)
    for i in range(0,len(e2)):
        if "∅" in e2[i]:
            return "∅"
        else:
            if "|" in e2:
                if len(e2[i])>1:
                    if e2[i][-1]=="*":
                        t = e2[i][:-1].split("|")
                        if t[0]==t[1]:
                            e2[i]=t[1]
                        elif t[1]=="λ":
                            e2[i]=t[0]+"*"
                    else:
                        t = e2[i].split("|")
                        if t[0]==t[1]:
                            e2[i]=t[1]
                        elif t[1]=="λ":
                            e2[i]=t[0]
    s = [s for s in e2 if "*" in s]
    for i in e2:
        if i+"*" in s:
            e2.remove(i)

    expresie="("
    for i in e2:
        expresie+=i
        expresie+=")"
        expresie+="("
    expresie=expresie[:-1]
    return expresie

def simplificare(expresie):
    e = expresie.find("|(")
    if reguli_simplificare(expresie[e+1:])=="∅":
        if expresie[:e]=="∅":
            return "∅"
        else:
            return expresie[:e]
    if expresie[1:e-1]=="λ":
        t1 = reguli_simplificare(expresie[e+1:])
        if "|" in t1:
            t2 = t1.split("|")
            if "λ" in t2[1]:
                return t2[0]+")*"+t2[1][4]
        return t
    elif expresie[1:e-1] in reguli_simplificare(expresie[e+1:]):
        t1 = reguli_simplificare(expresie[e + 1:])
        if "|" in t1:
            t2 = t1.split("|")
            if "λ" in t2[1]:
                return t2[0] + ")*" +t2[1][3:]
        return t
    return expresie[:e+1]+reguli_simplificare(expresie[e+1:])

def simplificare2(expresie):
    inc = expresie.find(")")
    nr=0
    for i in range(0,inc):
        if expresie[i]=="(":
            nr+=1
    nra=0
    i=inc
    while nr!=0:
        if expresie[i]==")":
            nr-=1
            nra+=1
        else:
            nra+=1
    x=inc+nra+1
    if expresie.find(expresie[:x],x+1)!=-1:
        return expresie[x+1:].split("|")[1]
    return expresie

intr1 = input("Introduceti starile A-0-B: ")
introduse = []
introduse.append(intr1.split('-'))
while intr1!='':
    intr1 = input()
    introduse.append(intr1.split('-'))
introduse.pop()
stari = {}
for i in introduse:
    if i[0] in stari.keys():
        stari[i[0]].update({i[1]:i[2]})
    else:
        stari.update({i[0]:{i[1]:i[2]}})

#λ ∅

alfabet = list(stari.keys())
nr_stari = len(stari)
tabel = [["-" for i in range(nr_stari**2)] for j in range(nr_stari+1)]
tabel_expresii = [["-" for i in range(nr_stari)] for j in range(nr_stari)]
tabel_nou = [["-" for i in range(nr_stari)] for j in range(nr_stari)]
print(stari)
t=0
for i in range(0,nr_stari):
    for j in range(0,nr_stari):
        if alfabet[j] in stari[alfabet[i]].values():
            if tabel[0][t]=="-" and i!=j:
                tabel[0][t]=list(stari[alfabet[i]].keys())[list(stari[alfabet[i]].values()).index(alfabet[j])]
                tabel_expresii[i][j] = tabel[0][t]
            elif tabel[0][t]=="-" and i==j:
                tabel[0][t] = list(stari[alfabet[i]].keys())[list(stari[alfabet[i]].values()).index(alfabet[j])]
                tabel[0][t] += "|λ"
                tabel_expresii[i][j] = tabel[0][t]
            t+=1
        elif i==j:
            tabel[0][t]="λ"
            tabel_expresii[i][j] = tabel[0][t]
            t+=1
        else:
            tabel[0][t]="∅"
            tabel_expresii[i][j] = tabel[0][t]
            t+=1

print(tabel[0])
print()
for k in range(1,nr_stari+1):
    col=0
    for i in range(0,nr_stari):
        for j in range(0,nr_stari):
            tabel[k][col]="("+tabel_expresii[i][j]+")"+"|"+"("+tabel_expresii[i][k-1]+")"+"("+tabel_expresii[k-1][k-1]+")"+"*"+"("+tabel_expresii[k-1][j]+")"
            if k==1:
                tabel[k][col]=simplificare(tabel[k][col])
            else:
                tabel[k][col]=simplificare2(tabel[k][col])
            tabel_nou[i][j]=tabel[k][col]
            col+=1
    print(tabel[k])
    print()
    tabel_expresii=copy.deepcopy(tabel_nou)


l = ""
for j in range(1,nr_stari):
    l = tabel[nr_stari][j-1]
print(l)
