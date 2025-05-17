

import tkinter as tk


root = tk.Tk()
root.geometry("400x600")
root.title("To Shop App")

monLabel = tk.Label(root, text="Months", font=("Arial", 20)).pack()
comButton = tk.Button(root, text="Common List").pack()


monthFrame = tk.Frame(root)
monthFrame.columnconfigure(0, weight=1)
monthFrame.columnconfigure(1, weight=1)
monthFrame.columnconfigure(2, weight=1)

mon1 = tk.Button(monthFrame, text="1").grid(row=0, column=0, sticky=tk.W+tk.E)
mon2 = tk.Button(monthFrame, text="2").grid(row=0, column=1, sticky=tk.W+tk.E)
mon3 = tk.Button(monthFrame, text="3").grid(row=0, column=2, sticky=tk.W+tk.E)

mon4 = tk.Button(monthFrame, text="4").grid(row=1, column=0, sticky=tk.W+tk.E)
mon5 = tk.Button(monthFrame, text="5").grid(row=1, column=1, sticky=tk.W+tk.E)
mon6 = tk.Button(monthFrame, text="6").grid(row=1, column=2, sticky=tk.W+tk.E)

mon7 = tk.Button(monthFrame, text="7").grid(row=2, column=0, sticky=tk.W+tk.E)
mon8 = tk.Button(monthFrame, text="8").grid(row=2, column=1, sticky=tk.W+tk.E)
mon9 = tk.Button(monthFrame, text="9").grid(row=2, column=2, sticky=tk.W+tk.E)

mon10 = tk.Button(monthFrame, text="10").grid(row=3, column=0, sticky=tk.W+tk.E)
mon11 = tk.Button(monthFrame, text="11").grid(row=3, column=1, sticky=tk.W+tk.E)
mon12 = tk.Button(monthFrame, text="12").grid(row=3, column=2, sticky=tk.W+tk.E)

monthFrame.pack(fill='x')



root.mainloop()