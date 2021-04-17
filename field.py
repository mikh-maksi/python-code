from tkinter import Tk, Canvas
import random
import time

root = Tk()
root.title("PythonicWay Quiz")

c = Canvas(root, width=800, height=400, bg="white")
c.grid()

circle = c.create_oval(150, 50, 100, 100, fill='green')

right_answer = c.create_text(150, 20,
                             font='Arial 20',
                             fill='green',
                             text="Рух у кімнаті"
                            )

right_answer1 = c.create_text(125, 120,
                             font='Arial 10',
                             fill='black',
                             text="30"
                            )
temperature = c.create_text(50, 220, font='Arial 10', fill='black',text=-270)
temp_color = c.create_rectangle(30, 400,80, 400 ,fill="#AAAAFF")
def bl():
    lv = int(random.random() * 200)

    if lv < 50:
        c.itemconfigure(circle, fill='green')
    else:
        c.itemconfigure(circle, fill='red')
    
    c.itemconfigure(right_answer1, text=lv)

    tm = int(random.random()*390-270)
    

    co = 400 - ((tm+270)/2.6)
    
    c.coords(temp_color,30, 400,80, co)
    if tm<-50:
        c.itemconfigure(temp_color, fill='#AAAAFF')
    if -50<=tm<0:
        c.itemconfigure(temp_color, fill='#AAFFAA')
    if 0<=tm<20:
        c.itemconfigure(temp_color, fill='#00FF00')
    if 20<=tm<60:
        c.itemconfigure(temp_color, fill='#FFFF00')
    if 60<=tm<=120:
        c.itemconfigure(temp_color, fill='#FF0000')        
    c.itemconfigure(temperature, text=tm)
    
    root.after(1000,bl)



bl()


root.mainloop()