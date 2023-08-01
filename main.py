import tkinter as tk
import os
import config
import random

def randomizer():
    randomp = random.randint(1,5)

    if randomp == 1:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(250, 300, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(470, 300, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(700, 300, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(950, 300, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(1200, 300, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(700, 500, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: button_click())
    elif randomp == 2:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(1200, 300, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(950, 300, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(700, 300, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(470, 300, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(250, 300, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(700, 500, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: button_click())
    elif randomp == 3:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(470, 300, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(700, 300, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(250, 300, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(1200, 300, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(950, 300, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(700, 500, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: button_click())
    elif randomp == 4:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(1200, 300, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(470, 300, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(950, 300, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(700, 300, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(250, 300, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(700, 500, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: button_click())
    elif randomp == 5:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(700, 300, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(250, 300, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(470, 300, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(950, 300, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(1200, 300, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(700, 500, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: button_click())

def button_click():
    randomizer()

def randomstory1():
    randomint = random.randint(1, 5)
    if randomint == 1:
        storytext = tk.Entry(root)
        storytext.insert("")
    if randomint == 2:
        storytext = tk.Entry(root)
        storytext.insert("")
    if randomint == 3:
        storytext = tk.Entry(root)
        storytext.insert("")
    if randomint == 4:
        storytext = tk.Entry(root)
        storytext.insert("")
    if randomint == 5:

root = tk.Tk()

root.geometry("500x500")
root.title("My Little Solar System")
root.configure(bg="black")

label = tk.Label(root,text="Welcome to the Solar System!", font=('Tw Cen MT', 18),fg="Purple",bg="Black")
label.pack(padx=5,pady=5)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

photocanvas = tk.Canvas(root,width=screen_width,height = screen_height)
photocanvas.pack()

bgdirectory = os.path.dirname(__file__)
#File paths for each planet png
bgpath = "SolarSystemResources\solarsystemgif.gif"
planet1 = "SolarSystemResources\Planet_1.png"
planet2 = "SolarSystemResources\Planet_2.png"
planet3 = "SolarSystemResources\Planet_3.png"
planet4 = "SolarSystemResources\Planet_4.png"
planet5 = "SolarSystemResources\Planet_5.png"
button = "SolarSystemResources\Button.png"
button_clicked = "SolarSystemResources\Button2.png"

bg_file_path = os.path.join(bgdirectory,bgpath)
p1fp = os.path.join(bgdirectory,planet1)
p2fp = os.path.join(bgdirectory,planet2)
p3fp = os.path.join(bgdirectory,planet3)
p4fp = os.path.join(bgdirectory,planet4)
p5fp = os.path.join(bgdirectory,planet5)
button1 = os.path.join(bgdirectory,button)
button2= os.path.join(bgdirectory,button_clicked)

background = tk.PhotoImage(file = bg_file_path)
p1 = tk.PhotoImage(file=p1fp)
p2 = tk.PhotoImage(file=p2fp)
p3 = tk.PhotoImage(file=p3fp)
p4 = tk.PhotoImage(file=p4fp)
p5 = tk.PhotoImage(file=p5fp)
b1 = tk.PhotoImage(file=button1)
b2 = tk.PhotoImage(file=button2)

background = background.zoom(5)
p1re = p1.zoom(5)
p2re = p2.zoom(5)
p3re = p3.zoom(5)
p4re = p4.zoom(5)
p5re = p5.zoom(5)
b1 = b1.zoom(1)
b2 = b2.zoom(1)


photocanvas.create_image(0, 0, image=background, anchor="nw")
newbutton = photocanvas.create_image(700,500,image=b1)
photocanvas.tag_bind(newbutton,'<Button-1>',lambda event: button_click())



root.mainloop()