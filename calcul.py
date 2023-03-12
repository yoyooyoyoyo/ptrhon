import tkinter as tk
from PIL import ImageTk


root = tk.Tk()
root.title("CHOI")
root.minsize(800, 600)

# Label
widget1 = tk.Label(root, text="이것은 Label입니다.")
widget1.pack()
# Button
img = ImageTk.PhotoImage(file="IMG_3213.jpg")
widget2 = tk.Label(root,image=img)
widget2.pack()
# Text
widget3 = tk.Text(root)
widget3.pack()
# Listbox
widget4 = tk.Listbox(root)
widget4.pack()


root.mainloop()

