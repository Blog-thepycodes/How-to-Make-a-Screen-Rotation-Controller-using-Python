from tkinter import *
import rotatescreen as rs
 
 
def rotate_screen(orientation):
    screen = rs.get_primary_display()
    if orientation == "up":
        screen.set_landscape()
    elif orientation == "right":
        screen.set_portrait_flipped()
    elif orientation == "left":
        screen.set_portrait()
    elif orientation == "down":
        screen.set_landscape_flipped()
 
 
def reset_screen():
    screen = rs.get_primary_display()
    screen.set_landscape()
 
 
root = Tk()
root.geometry("500x250")
root.title("Screen Rotation Controller - The Pycodes")
root.configure(bg="lightblue")
 
frame = Frame(root, bg="lightblue")
frame.pack(pady=30)
 
Button(frame, text="UP", command=lambda: rotate_screen("up"), bg="white", font="arial 14", width=20).grid(row=0, column=0, padx=10)
Button(frame, text="Right", command=lambda: rotate_screen("right"), bg="white", font="arial 14", width=20).grid(row=0, column=1, padx=10)
Button(frame, text="Left", command=lambda: rotate_screen("left"), bg="white", font="arial 14", width=20).grid(row=1, column=0, padx=10)
Button(frame, text="Down", command=lambda: rotate_screen("down"), bg="white", font="arial 14", width=20).grid(row=1, column=1, padx=10)
Button(root, text="Reset the Screen", command=reset_screen, bg="white", font="arial 14", width=30).pack()
 
root.mainloop()
