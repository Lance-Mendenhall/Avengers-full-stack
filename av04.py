import sqlite3
import tkinter as tk
import tkinter.font as font
import random
window = tk.Tk()
frame1 = tk.Frame(master=window)
frame2 = tk.Frame(master=window)
frame3 = tk.Frame(master=window)
frame4 = tk.Frame(master=window)
frame5 = tk.Frame(master=window)
myFont = font.Font(size=16)
# label1 = tk.Label(frame4, text="Choose your warrior!", bg="blue", fg="yellow",bd=10)
# label2 = tk.Label(frame4, text="Choose your warrior!", bg="blue", fg="yellow",bd=10)
label3 = tk.Label(frame5, text="Results", bg="blue", fg="yellow", font=myFont)
# label99 = tk.Label(frame4, bg="white", fg="white", bd=20)
window.title("Super combat!")
window.geometry("700x700")
name1 = "Bob"
name2 = "Fred"


buttonList = []
connection = sqlite3.connect("contestants.db")
cursor = connection.cursor()
rows = cursor.execute(
    "SELECT NAME, bg, fg, powerlevel from fighters").fetchall()

counter = 0
pl1 = 0
pl2 = 0


def buttSel(ndp):  # ndp = nom de plume
    # print("You clicked",ndp)
    global counter, pl1, pl2, name1, name2

    output1 = cursor.execute(
        "select powerlevel from fighters where name = ?", (ndp,)).fetchall()
    c1 = output1[0][0]
    if counter == 0:
        # set fighter 1 in label 1
        pl1 = c1
        counter += 1
        con1.config(text=ndp)
        # print(c1)
        name1 = ndp

    elif counter == 1:
        # set fighter 2 in label 2
        pl2 = c1
        counter = 0
        con2.config(text=ndp)
        # print(c1)
        name2 = ndp
    # print(c1)


def fight():
    dw = " "  # display winner
    global pl1, pl2, name1, name2
    j = random.random()
    f1result = int(j * 10) + 1 + pl1
    j = random.random()
    f2result = int(j * 10) + 1 + pl2
    # print("f1r: ",f1result," f2r: ",f2result," pl1:",pl1," pl2:",pl2)
    if f1result > f2result:
        # print(name1,"wins!")
        dw = name1 + " wins!"
        label3.config(text=dw)
    elif f2result > f1result:
        # print(name2,"wins")
        dw = name2 + " wins!"
        label3.config(text=dw)
    else:
        # print("Tie!")
        label3.config(text="Tie")

        # label1.config(text = ndp)


for x in rows:
    name = x[0]
    bgg = x[1]
    fgg = x[2]
    pl = x[3]

    b = tk.Button(
        frame1,
        text=name,
        width=20,
        height=5,
        bg=bgg,
        fg=fgg,
        command=lambda arg1=name: buttSel(arg1)
    )
    buttonList.append(b)

myrow = 0
mycolumn = 0

for mybutt in buttonList:
    mybutt.grid(row=myrow, column=mycolumn)
    mycolumn += 1
    if mycolumn > 7:
        mycolumn = 0
        myrow += 1

con1 = tk.Label(
    master=frame2,
    text="Contestant 1",
    width=40,
    height=10,
    fg="white",
    bg="#800033",
    font=myFont
)

con2 = tk.Label(
    master=frame2,
    text="Contestant 2",
    width=40,
    height=10,
    fg="white",
    bg="#004d99",
    font=myFont
)
con1.grid(row=0, column=0)
con2.grid(row=0, column=1)

fb = tk.Button(
    master=frame3,
    text="Fight!",
    width=20,
    height=5,
    bg="gray",
    fg="black",
    command=lambda: fight()
)
fb.pack()

# frame2['padding'] = (0,0,10,10)


# label1.grid(row=0,column=0)
# label99.grid(row=0,column=1)
# label2.grid(row=0,column=2)
label3.pack()

frame1.pack()
frame2.pack(pady=(10, 10))
frame3.pack()
# frame4.pack(pady=(10,10))
frame5.pack(pady=(10, 10))


window.mainloop()
