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
alfabet = list(stari.keys())
nr_stari = len(stari)
print("Nr stari AFD: "+ str(nr_stari))
tabel = [["-" for i in range(nr_stari-1)] for j in range(nr_stari-1)]
for i in range(0,nr_stari-1):
    for j in range(0,nr_stari-1):
        if j == nr_stari-i:
            continue
        if j > nr_stari-i:
            continue
        if "sf" in list(stari[alfabet[i]].values()) and "sf" not in list(stari[alfabet[nr_stari-j-1]].values()):
            tabel[i][j]='*'
        elif "sf" in list(stari[alfabet[nr_stari-j-1]].values()) and "sf" not in list(stari[alfabet[i]].values()):
            tabel[i][j]='*'

while True:
    nr=0
    for i in range(0,nr_stari-1):
        for j in range(0,nr_stari-1-i):
            if tabel[i][j]=='*':
                continue
            else:
                z = []
                x = list(stari[alfabet[i]].keys())
                y = list(stari[alfabet[-j-1]].keys())
                for k in x:
                    if k in y:
                        z.append([stari[alfabet[i]][k],stari[alfabet[-j-1]][k]])
                for k in z:
                    if k[0]!=k[1]:
                        if tabel[alfabet.index(k[0])-1][alfabet.index(k[1])-1] == '*' or tabel[alfabet.index(k[1])-1][alfabet.index(k[0])-1]:
                            tabel[i][j]='*'
    if nr==0:
        break

stari_minimale={}
com = []
for i in range(0,nr_stari-1):
    for j in range(0,nr_stari-1-i):
        if tabel[i][j]!='*':
            com.append([alfabet[i],alfabet[j]])
            alfabet.remove(alfabet[i])
            alfabet.remove(alfabet[j-1])

for i in alfabet:
    stari_minimale.update({i:stari[i]})
for i in com:
    stare = str(i[0])+ str(i[1])
    z=[]
    min=[]
    x = list(stari[i[0]].keys())
    y = list(stari[i[1]].keys())
    for k in x:
        z.append([stari[i[0]][k],stari[i[1]][k]])
    for k in z:
        if k[0]==k[1]:
            min.append(k[0])
        else:
            min.append(str(k[0])+str(k[1]))
    stari_minimale.update({stare:min})
print(stari_minimale)
print("Nr stari AFD minimal: " + str(len(stari_minimale)))
