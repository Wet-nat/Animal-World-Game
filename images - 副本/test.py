from tkinter import *
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("2048x1280")
  
# Add image file
bg = PhotoImage(file = "menu.PNG")
  
# Create Canvas
canvas1 = Canvas( root, width = 2048,
                 height = 1280)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
root.mainloop()