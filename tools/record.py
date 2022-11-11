import os
import csv
from datetime import datetime
directory = os.path.abspath("./record")#檔案路徑
if not os.path.isdir(directory):#建立根目錄
    os.makedirs(directory)
filname_abs=None
def recordData(distance,lightValue):
    global filename_abs
    current = datetime.now()#現在時間
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")#現在時間檔名    
    currentFiles = os.listdir(directory)
    filename_abs = f"{directory}/{filename}"
    if filename not in currentFiles:#建立檔案
        file = open(filename_abs,'w',encoding='utf-8',newline='')
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
        #加入資料
    with open(filename_abs,"a",newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue])
        #將資料放到firestore
        print("要加入的資料")
        print("日期",current.strftime("%Y-%m-%d %H:%M:%S"))
        print("距離",distance)
        print("光線",lightValue)
def getData():
    with open(filename_abs,"r",newline='') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    return data