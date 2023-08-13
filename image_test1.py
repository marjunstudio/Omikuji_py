import tkinter as tk
import os.path

# メインウィンドウ
root  = tk.Tk()

# フレーム
frame = tk.Frame(root)
frame.pack()

image_path = "images/radio1.png"
dir_path = os.path.dirname(__file__)
image_path = os.path.join(dir_path, image_path)
my_image = tk.PhotoImage(file=image_path)

# ラベルに表示
label = tk.Label(frame, image=my_image)
label.pack()

root.mainloop()
