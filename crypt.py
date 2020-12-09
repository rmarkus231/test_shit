#kodeerija

letterNum = {
    "#":"##",
    "a":"01",
    "b":"02",
    "c":"03",
    "d":"04",
    "e":"05",
    "f":"06",
    "g":"07",
    "h":"08",
    "i":"09",
    "j":"10",
    "k":"11",
    "l":"12",
    "m":"13",
    "n":"14",
    "o":"15",
    "p":"16",
    "q":"17",
    "r":"18",
    "s":"19",
    "š":"20",
    "z":"21",
    "ž":"22",
    "t":"23",
    "u":"24",
    "v":"25",
    "w":"26",
    "õ":"27",
    "ä":"28",
    "ö":"29",
    "ü":"30",
    "x":"31",
    "y":"32",
}
reversed_letterNum = {value : key for (key, value) in letterNum.items()}

singleNum= {
    "01":"1",
    "02":"2",
    "03":"3",
    "04":"4",
    "05":"5",
    "06":"6",
    "07":"7",
    "08":"8",
    "09":"9",
}
reversed_singleNum = {value : key for (key, value) in singleNum.items()}

täis=["a","e","i","o","u","õ","ä","ö","ü"]
sulg=["k","p","t","g","b","d"]
nine=["a","b","c","d","e","f","g","h","i"]

#eemaldab nth tähe
def remove(string, h):  
  
    for j in range(len(string)): 
        if j == h:
            string = string.replace(string[h], "", 1) 
    return string

def removeDot(string):
    string,x=string.split(".")
    return string

#teeb stringi arvuks ja kontrollib kas täishäälik ja jagav 2ga
def arvuta(string):
    if reversed_letterNum[string] in nine and int(singleNum[string]) == 2:
        return "##"
    else:
        if reversed_letterNum[string] in täis:
            if reversed_letterNum in nine:
                p=reversed_singleNum[string]
                p=int(p)
            else:
                p=singleNum[string]
                p=int(p)
            if p % 2 ==1:
                p=p+1
            pdiv=p/2
            if pdiv < 10:
                pdiv=reversed_singleNum[removeDot(str(pdiv))]
                return pdiv
            else:
                pdiv=str(p)
        else:
            if reversed_letterNum in nine:
                p=reversed_singleNum[string]
                p=int(p)
            else:
                p=int(string)
            if p % 2 ==1:
                p=p-1
                pdiv=p/2
            else:
                pdiv=p/2
            if pdiv < 10:
                pdiv=reversed_singleNum[removeDot(str(pdiv))]
                return pdiv
            else:
                pdiv=removeDot(str(pdiv))
                return pdiv

sõna=input("to translate: ")
sõna=sõna.lower()
#täishäälik esimeseks täheks sõnas
y=0
if sõna[0] not in täis:
    for i in range(len(sõna)):
        if sõna[y] in täis:
            if i < 10:
                hn=reversed_letterNum[reversed_singleNum[str(y+1)]]
            sõna1=sõna[y]+remove(sõna,y)+hn
        else:
            y=y+1

#vahetab iga tähe tähestikku järjekorra numbriga
num=""
for i in range(len(sõna1)):
    x=letterNum[sõna1[i]]
    num=num+str(x)
#eristab iga tähe numbrid massiivi
z=0
n=[]
n2=[]
while z+2 <= len(num):
    n.append(num[z:z+2])
    z=z+2
for i in range(len(n)):
    n2.append(arvuta(n[i]))

w=""
for i in range(len(n2)):
    w=w+reversed_letterNum[n2[i]]
print(w)