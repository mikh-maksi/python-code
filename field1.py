from tkinter import Tk, Canvas
import random
import time

root = Tk()
root.title("Dashboard")

c = Canvas(root, width=800, height=600, bg="white")
c.grid()

circle = c.create_oval(150, 50, 100, 100, fill='green')

move = c.create_text(150, 20,
                             font='Arial 10',
                             fill='green',
                             text="Рух у кімнаті"
                            )

Temperature_text = c.create_text(50, 180,
                             font='Arial 10',
                             fill='green',
                             text="Температура"
                            )

move_power = c.create_text(125, 120,
                             font='Arial 10',
                             fill='black',
                             text="30"
                            )
temperature = c.create_text(50, 220, font='Arial 10', fill='black',text=-270)
temp_color = c.create_rectangle(30, 400,80, 230 ,fill="#AAAAFF")

dry = c.create_rectangle(250, 270, 500, 230 ,fill="#AAFFAA")
 
dry_level = 40
dry1 = c.create_rectangle(250, 270, 250+dry_level*2.5, 230 ,fill="#FFFFAA")




def bl():
    lv = int(random.random() * 200)

    if lv < 50:
        c.itemconfigure(circle, fill='green')
    else:
        c.itemconfigure(circle, fill='red')
    
    c.itemconfigure(move_power, text=lv)

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



#bl()


root.mainloop()