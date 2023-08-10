import tkinter as tk
from tkinter import *
import requests
from PIL import ImageTk, Image
import math 
from datetime import datetime
import time 
root = tk.Tk()
root.geometry("1000x900")
root['background']='#CCFFFF'
root.title("Welcome")
#define function
def resize_image(image, new_width, new_height):
    resized_image = image.resize((new_width, new_height))
    return resized_image



# clock animation
WIDTH = 150
HEIGHT = 150
clock_frame = Frame(root, bg='#CCFFFF' )
clock_frame.pack(anchor='ne', padx=20, pady=20)
canvas = tk.Canvas(clock_frame, width=WIDTH, height=HEIGHT, bg=clock_frame['bg'], highlightthickness=0)
canvas.pack()
def update_clock():
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec
 
    # Draw clock face
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)
    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica", 12))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))
 
    # Draw minute lines
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
 
    # Draw hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="black", width=6)
 
    # Draw minute hand
    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="black", width=4)
 
    # Draw second hand  
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)
 
    canvas.after(1000, update_clock)
update_clock()

def date_time():
    now = datetime.now()
    date_string = now.strftime("%A, %d %B %Y")
    date_label.config(text=date_string)
    date_label.after(1000, date_time)
date_label = Label(clock_frame, font=('Lato-Black', 14), bg='#CCFFFF')
date_label.pack(pady = 10)
date_time()


# frame parent {
frame = tk.Frame(root, bg='#CCFFFF')
frame.pack(side='top', fill=None, expand = False)

#image
image = Image.open("DUT.jpg")
resize_img = resize_image(image, 110, 100)
tk_img = ImageTk.PhotoImage(resize_img)
image_label = Label(frame, image=tk_img)
#image_label.grid(row = 1, column = 0)
image_label.pack()


sb_label = tk.Label(frame, text = "Smart Building", font=("Lato-Black", 30, 'italic'), fg = 'blue', bg='#CCFFFF')
sb_label.pack(pady=50)

# child frame
frame2 = Frame(frame, bg='#CCFFFF')
frame2.pack(pady=50)

wc_label = tk.Label(frame2, text="WELCOME", bg='blue', fg='yellow', font=('Lato-Black', 24), padx=200)
wc_label.pack()

lb3 = tk.Label(frame2, text="           ", bg='yellow', fg='black', font=('Lato-Black', 24), padx=80)
lb3.pack()

dut_label = tk.Label(frame2, text=" to DUT", bg = 'red', fg='yellow', font=('Lato-Black', 24), padx=60)
dut_label.pack()
#}


# hàm update name
    
def inf_loop():
    with open("log.txt", "r") as file:
        last_line = file.readlines()[-1]
        name_list = last_line
        lb3.config(text=name_list)
    root.after(100, inf_loop)
    
requests_url = 'http://127.0.0.1:4040/name'

def loop():
    name_list=requests.post(requests_url).json()  
    lb3.config(text=name_list)
    root.after(100, loop)  
loop() 
root.mainloop()
