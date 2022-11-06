# Microbit-Termostat
Projektni zadatak iz informatike

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import json
    
data = {"1":{"2.11.2022.":{"14:30":"19", "15:00":"20"}, "3.11.2022.":{"14:30":"11", "15:00":"21"}}, "2":{"2.11.2022.":{"14:30":"19", "15:00":"22"}, "3.11.2022.":{"14:30":"11", "15:00":"12"}}}
data = {"1":{"2.11.2022.":{"14:30":"4", "15:00":"5"}, "3.11.2022.":{"14:30":"6", "15:00":"7"}}, "2":{"2.11.2022.":{"14:30":"14", "15:00":"15"}, "3.11.2022.":{"14:30":"16", "15:00":"17"}}, "3":{"2.11.2022.":{"14:30":"24", "15:00":"25"}, "3.11.2022.":{"14:30":"26", "15:00":"27"}}}

wb = Workbook()
ws = wb.active
ws.title = "Temperature"

br_ap = 1

temperature = []
vremena = []

for microbit, dan in data.items():
    for dan, vrijeme in data[microbit].items():
        for vrijeme, temperatura in data[microbit][dan].items():
            temperature.append(temperatura)
            vremena.append(vrijeme)
            M = int(microbit)

def my_function(x):
  return list(dict.fromkeys(x))
vremena = my_function(vremena)

n = len(vremena)
br = 0
brp = 1
m = (len(temperature)//M)
p = m
lista = []

for microbit in data:
    for i in range(0, len(vremena)):
        vrijeme = vremena[i]
        for j in range(0, len(vremena)-1):
            temp = temperature[br:m:n]
            temp = [eval(i) for i in temp]
            if brp % 2 != 0:
                br += 1 
            if brp % 2 == 0:
                br = m
                m = m + p
            brp += 1
            temp.insert(0, vrijeme)
            print(temp)
            lista.append(temp)

l = 0
            
for microbit in data:
    mic = ['MICROBIT_' + microbit]
    ws.append([''] + mic)
    
    datumi = [''] + list(data[microbit].keys())
    ws.append(datumi)
    
    br_ap2 = br_ap + 1
    ws.merge_cells(f"{'A' + str(br_ap)}:{'A' + str(br_ap2)}")

    for i in range(0, n):
        ws.append(lista[l])
        l += 1
    ws.append([''])
    ws.append([''])
    br_ap += 4


wb.save("NovTemp.xlsx")
