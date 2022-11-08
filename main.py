import tkinter as tk #建立視窗用
from datetime import datetime #使間使用
from tools import data,record #tools裡面的套件
class Window(tk.Tk):#視窗介面
    def __init__(self):
        super().__init__()   
        self.label = tk.Label(self,text="",font=("arial",30))
        self.label.pack(padx=50,pady=30)
        self.change_time()
        self.window_time()
        
        
    def change_time(self): #顯示現在時間用
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.label.config(text=now_str)
        self.after_id = self.label.after(1000,self.change_time)

    def window_time(self):
        distance = data.getDistance()
        print(distance)
        if distance < 100.0: 
            print(f"距離:{distance:.2f}公分")
        else:
            print(f"距離:大於100公分")
            distance = 100

        lightValue = data.getLightValue()
        print(f"光線:{lightValue:.1f}")
        record.recordData(distance=100,lightValue=200)

        
        self.window_id = self.after(1000 * 30,self.window_time)

    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.after_cancel(self.window_id)
        self.destroy()
        
        
        
def main():#執行程式
    window =  Window()
    window.title("數位時鐘")
    window.protocol("WM_DELETE_WINDOW",window.delete_delay)
    window.mainloop()
if __name__ == "__main__":
    main()