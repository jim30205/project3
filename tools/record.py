import os
from datetime import datetime
directory = os.path.abspath("./record")#檔案路徑
if not os.path.isdir(directory):#建立根目錄
    os.makedirs(directory)
def recordData(distance,lightValue):
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")    
    currentFiles = os.listdir(directory)
    if filename not in currentFiles:
        print(f"沒有{filename}此檔")