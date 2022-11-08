import os

directory = os.path.abspath("./record")
if not os.path.isdir(directory):
    os.makedirs(directory)
def recordData(distance,lightValue):
    print("紀錄")