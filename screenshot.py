import time
import pyautogui
import tkinter as tk


def screenshot():
    image_name = int(round(time.time() * 1000))
    image_name = "outputs/{}.png".format(image_name)
    time.sleep(5)
    img = pyautogui.screenshot(image_name)
    img.show()

#screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame, 
    text= "Take a Screenshot",
    command= screenshot
    )

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text= "CLOSE",
    command= quit
)
close.pack(side=tk.LEFT)

root.mainloop()