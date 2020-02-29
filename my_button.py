# Reminder button by Heidi Bada
# modified from lambda function exercise
# in Colt Steele's Modern Python course on udemy.com

import tkinter as tk

# set up tkinter
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# create button that stays on screen as a reminder
msg = input('What do you need to do soon?')
button = tk.Button(frame,
                   text=msg,
                   fg="red",
                   command=lambda: print("Don't forget to " + msg))

# supporting code
button.pack(side=tk.LEFT)
root.mainloop()
