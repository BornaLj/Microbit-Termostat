#za testiranje
data = [["1", "2.11.2022.", "14:55", "19"], ["2", "2.11.2022.", "14:55", "19"], ["1", "2.11.2022.", "15:00", "20"], ["1", "3.11.2022.", "10:00", "11"], ["3", "3.11.2022.", "20:00", "15"]]

#mora biti: data = {"1":{"2.11.2022.":{"14:55":"19", "15:00":"20"}, "3.11.2022.":{"10:00":"11"}}, "2":{"2.11.2022.":{"14:55":"19"}}}

newData = {}
newData2 = {}
lista = []
rječnik = {}
rješeno = False

for x in range(len(data)):
    lista.append(int(data[x][0]))

n = max(lista)

lista = []

for i in range(1, n+1):
    lista = []
    for j in data:
        if int(j[0]) == i:
            lista.append(j[1:])
    newData.update({str(i):lista})

for a,b in newData.items():
    rječnik = {}
    zapis = {}
    for c in range(len(b)):
        if rješeno == True:
            rješeno = False
            continue
        else:
            try:
                if b[c][0] == b[c+1][0]:
                    datum = b[c][0]
                    rješeno = True
                    zapis = {datum:{b[c][1]:b[c][2], b[c+1][1]:b[c+1][2]}}
                    rječnik.update(zapis)
                else:
                    datum = b[c][0]
                    zapis = {datum:{b[c][1]:b[c][2]}}
                    rječnik.update(zapis)
            except:
                datum = b[c][0]
                zapis = {datum:{b[c][1]:b[c][2]}}
                rječnik.update(zapis)
                continue
    newData2.update({a:rječnik})

data = newData2.copy()