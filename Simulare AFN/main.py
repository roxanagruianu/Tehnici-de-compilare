stari  = {
    "A": {
        "0":"B",
        "1":"D"
    },
    "B":{
        "0": ["B","C"],
        "1": "B"
    },
    "C": {
        "": "sf"
    },
    "D":{
        "0": "D",
        "1": ["D","C"],
        "": "sf"
    }
}


cuvant = input("Introduceti cuvant: ")
lung = len(cuvant)
starecurenta = ["A"]
print(starecurenta)
for i in cuvant:
    stareurmatoare = []
    for j in starecurenta:
        for k in stari[j]:
            if k == i:
                if isinstance(stari[j][k],list):
                    for l in stari[j][k]:
                        stareurmatoare.append(l)
                else:
                    stareurmatoare.append(stari[j][k])
    starecurenta = stareurmatoare
    print(starecurenta)

nr=0
for i in starecurenta:
    for j in stari[i]:
        if j == "":
            nr=nr+1
if nr>0:
    print("Recunoscut")
else:
    print("Nerecunoscut")

