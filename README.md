# Microbit-Termostat
Projektni zadatak iz informatike

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import json

for microbit in data:
    ws.append([''] + [microbit])
    
    datumi = [''] + list(data[microbit].keys())
    ws.append(datumi)
    
    for col in range(1, len(data['MICROBIT_1']) + 1):
        char = get_column_letter(col)
        br_ap = 1
        br_ap2 = br_ap + 1
        ws.merge_cells(f"{'A' + str(br_ap)}:{'A' + str(br_ap2)}")
        

    for dan in microbit:

        for vrijeme in dan:

            for temperatura in vrijeme:
                temperature = []
                temperature.append(data[microbit][dan][vrijeme])
                ws.append(vrijeme + temperature)
                
    br_ap += 1
        
    ws.append([''])
    ws.append([''])


wb.save("NovTemp.xlsx")
