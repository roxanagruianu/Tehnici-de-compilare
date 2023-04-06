from itertools import groupby

litere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
T = ['num','id','+','-','/','*','(',')']
N = ["E","T","E'","T'","F"]

p = input()
if not p:
    print("Expresie incorecta sintactic!")
    exit()

p1 = []
for i in p:
    if i in litere:
        p1.append('id')
    else:
        p1.append(i)

text = []
for i in range(0,len(p1)):
    if p1[i].isnumeric():
        text.append('num')
    else:
        text.append(p1[i])
text = [x[0] for x in groupby(text)]
for i in text:
    if i not in T:
        print("Expresie incorecta sintactic!")
        exit()
for i in range(0,len(text)):
    for j in range(i,len(text)):
        if text[i]=="+" and text[j]=="+":
            print("Expresie incorecta sintactic!")
            exit()
        elif text[i]=="-" and text[j]=="-":
            print("Expresie incorecta sintactic!")
            exit()
        elif text[i]=="*" and text[j]=="*":
            print("Expresie incorecta sintactic!")
            exit()
        elif text[i]=="*" and text[j]=="*":
            print("Expresie incorecta sintactic!")
            exit()
        elif text[i]=="id" and text[j]=="id":
            print("Expresie incorecta sintactic!")
            exit()

def reguli(r,u):
    if r=="E":
        return "TE'"
    elif r=="E'":
        if u=="+":
            return "+TE'"
        elif u=="-":
            return "-TE'"
        elif u=='':
            return ''
    elif r=="T":
        return "FT'"
    elif r=="T'":
        if u=="*":
            return "*FT'"
        elif u=="/":
            return "/FT"
        elif u=='':
            return ''
    elif r=="F":
        if u=="(":
            return "(E)"
        elif u=="id":
            return "id"
        elif u=="num":
            return "num"

#R1 : E -> TE'
#R2 : E' -> +TE'|-TE'|''
#R3 : T - > FT'
#R4 : T' -> *FT'|/FT'|''
#R5 : F -> (E)|id|num

i = len(text)

derivare = []


def functie_derivare(text,lit):
    global i
    global derivare,d1,d2,d3
    if lit=="E":
        derivare.append("E")
        if functie_derivare(text,"T"):
            if functie_derivare(text,"E'"):
                return 1
            else:
                return 0
        else:
            return 0
    elif lit=="E'":
        derivare.append("E'")
        if text[-i]=="+":
            derivare.append("+")
            i-=1
            if i==0 or i<0:
                print("Expresie incorecta sintactic!")
                exit()
            else:
                if functie_derivare(text,"T"):
                    if functie_derivare(text,"E'"):
                        return 1
                    else:
                        return 0
                else:
                    return 0
        elif text[-i]=="-":
            derivare.append("-")
            i-=1
            if i==0 or i<0:
                print("Expresie incorecta sintactic!")
                exit()
            else:
                if functie_derivare(text,"T"):
                    if functie_derivare(text,"E'"):
                        return 1
                    else:
                        return 0
                else:
                    return 0
        else:
            derivare.append(" ")
            return 1
    elif lit=="T":
        derivare.append("T")
        if functie_derivare(text,"F"):
            if functie_derivare(text,"T'"):
                return 1
            else:
                return 0
        else:
            return 0
    elif lit=="T'":
        derivare.append("T'")
        if text[-i]=="*":
            derivare.append("*")
            i -= 1
            if i == 0 or i < 0:
                print("Expresie incorecta sintactic!")
                exit()
            else:
                if functie_derivare(text,"F"):
                    if functie_derivare(text,"T'"):
                        return 1
                    else:
                        return 0
                else:
                    return 0
        elif text[-i]=="/":
            derivare.append("/")
            i -= 1
            if i == 0 or i < 0:
                print("Expresie incorecta sintactic!")
                exit()
            else:
                if functie_derivare(text,"F"):
                    if functie_derivare(text,"T'"):
                        return 1
                    else:
                        return 0
                else:
                    return 0
        else:
            derivare.append(" ")
            return 1
    elif lit=="F":
        derivare.append("F")
        if text[-i]=="(":
            derivare.append("(")
            i -= 1
            if i == 0 or i < 0:
                print("Expresie incorecta sintactic!")
                exit()
            else:
                if functie_derivare(text,"E"):
                    if text[-i]==")":
                        derivare.append(")")
                        i-=1
                        return 1
                    else:
                        return 0
                else:
                    return 0
        elif text[-i]=="id":
            derivare.append("id")
            i-=1
            return 1
        elif text[-i]=="num":
            derivare.append("num")
            i-=1
            return 1
        else:
            return 0

def functie_terminale(temp):
    if temp.startswith("id"):
        if temp[3]=="'":
            return 4
        else:
            return 3
    elif temp.startswith("num"):
        if temp[4]=="'":
            return 5
        else:
            return 4
    elif temp.startswith("("):
        return 2
    elif temp.startswith(")"):
        return 2
    elif temp.startswith("+"):
        if temp[2]=="'":
            return 3
        else:
            return 2
    elif temp.startswith("-"):
        if temp[2]=="'":
            return 3
        else:
            return 2
    elif temp.startswith("*"):
        if temp[2] == "'":
            return 3
        else:
            return 2
    elif temp.startswith("/"):
        if temp[2] == "'":
            return 3
        else:
            return 2
    elif temp[1]=="'":
        return 2
    else:
        return 1

if functie_derivare(text,"E"):
    if i==0:
        output_derivare = 'E->'
        terminale_derivare = ''
        d = ["E"]
        temp ='E'
        for i in range(0, len(derivare) - 1):
            if derivare[i] in T:
                terminale_derivare += derivare[i]
            elif derivare[i]==" ":
                continue
            elif derivare[i + 1] in N:
                d.append(reguli(derivare[i], ""))
                if len(temp)>1:
                    nr = functie_terminale(temp)
                    temp = reguli(derivare[i],"") + temp[nr:]
                else:
                    temp = reguli(derivare[i],"")
                output_derivare += terminale_derivare
                output_derivare += temp
                output_derivare += "->"
            elif derivare[i + 1] in T:
                d.append(reguli(derivare[i], derivare[i + 1]))
                nr=functie_terminale(temp)
                temp = reguli(derivare[i], derivare[i+1]) + temp[nr:]
                output_derivare += terminale_derivare
                output_derivare += temp
                output_derivare += "->"
            elif derivare[i+1]==" ":
                d.append(reguli(derivare[i],''))
                output_derivare += terminale_derivare
                nr = functie_terminale(temp)
                temp = temp[nr:]
                output_derivare += temp
                output_derivare += "->"
        if derivare[len(derivare)-1]==" ":
            if not temp:
                temp=''
            elif temp[-1]=="'":
                temp=temp[:-2]
            else:
                temp=temp[:-1]
            output_derivare+=terminale_derivare
            output_derivare+=temp
        print(output_derivare)
    else:
        print("Expresie incorecta sintactic!")
else:
    print("Expresie incorecta sintactic!")
