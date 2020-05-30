import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter.font as tkFont

root = tk.Tk()
root.geometry('600x500+100+200',)
root.title('Electronics Calculator')
root.configure(bg='#7ca2a2')

number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.IntVar()
number6 = tk.StringVar()

# Functions for calculating gain
# Inverting Op-Amp Gain
def callresult(label_gain, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    gain = int(num1) / int(num2)
    label_gain.config(text="Gain is -%d" % gain)
    return

# Non Inverting Op-Amp Gain
def callresult1(label_gain1, n3, n4):
    num3 = (n3.get())
    num4 = (n4.get())
    gain = 1 + int(num3)/int(num4)
    label_gain1.config(text="Gain is %d" % gain)
    return

# Resistors in parallel
def callresult2(n5, n6):
    entry_list = ''
    #num5 = (n5.get())
    #num6 = (n6.get())
    for entries in my_entries:
        result = result + num6
    label_result.config(text="Results is %d" % result)
    return


# Functions used for erasing screen
def Delete_Inverting():
    myLabel.pack_forget()
    labelNum1.pack_forget()
    entryNum1.pack_forget()
    labelNum2.pack_forget()
    entryNum2.pack_forget()
    labelGain.pack_forget()
    buttonCal.pack_forget()

def Delete_NonInverting():
    myLabel.pack_forget()
    labelNum3.pack_forget()
    entryNum3.pack_forget()
    labelNum4.pack_forget()
    entryNum4.pack_forget()
    labelGain1.pack_forget()
    buttonCal1.pack_forget()
    labelGain1.pack_forget()


my_entries = []


def comboClick(event):
    global myLabel,labelNum1,entryNum1,labelNum2,entryNum2,labelGain,buttonCal,labelNum3,entryNum3,labelNum4,entryNum4,labelGain1,buttonCal1,labelGain1

    myLabel = Label(root, text=myCombo.get())
    myLabel.pack(pady=5)

    if myCombo.get() == "Inverting Op-Amp":
        # Inverting Amp
        labelNum1 = tk.Label(root, text="Enter Feedback Resistor", bg="#808080")
        labelNum1.pack(pady=10)
        entryNum1 = tk.Entry(root, textvariable=number1)
        entryNum1.pack(pady=10)
        labelNum2 = tk.Label(root, text="Enter Ground Resistor", bg="#808080")
        labelNum2.pack(pady=10)
        entryNum2 = tk.Entry(root, textvariable=number2)
        entryNum2.pack(pady=10)
        labelGain = tk.Label(root, bg="#7ca2a2")

        call_result = partial(callresult, labelGain, number1, number2)
        buttonCal = tk.Button(root, text="Calculate", command=call_result, bg="#fd9014")
        buttonCal.pack()
        labelGain.pack(pady=5)
        DeleteButton = Button(root, text="Delete Text", command=Delete_Inverting)
        DeleteButton.pack(pady=10)

    if myCombo.get() == "Non Inverting Op-Amp":
        # Non Inverting Amp
        labelNum3 = tk.Label(root, text="Enter Feedback Resistor", bg="#808080")
        labelNum3.pack(pady=10)
        entryNum3 = tk.Entry(root, textvariable=number3)
        entryNum3.pack(pady=10)
        labelNum4 = tk.Label(root, text="Enter Ground Resistor", bg="#808080")
        labelNum4.pack(pady=10)
        entryNum4 = tk.Entry(root, textvariable=number4)
        entryNum4.pack(pady=10)
        labelGain1 = tk.Label(root, bg="#7ca2a2")

        call_result1 = partial(callresult1, labelGain1, number3, number4)
        buttonCal1 = tk.Button(root, text="Calculate", command=call_result1, bg="#fd9014")
        buttonCal1.pack()
        labelGain1.pack(pady=5)
        DeleteButton2 = Button(root, text="Delete Text", command=Delete_NonInverting)
        DeleteButton2.pack(pady=10)

    if myCombo.get() == "Resistors in Parallel":
        # Resistors in parallel
        labelNum5 = tk.Label(root, text="How many resistors would you like to enter?", bg="#808080")
        labelNum5.pack(pady=10)
        entryNum5 = tk.Entry(root, textvariable=number5)
        entryNum5.pack(pady=10)
        labelNum6 = tk.Label(root, text="Enter Resistors", bg="#808080")
        labelNum6.pack(pady=10)
        num_resistors = int(entryNum5.get())
        for x in range(num_resistors):
            my_entry = Entry(root)
            my_entry.pack(pady=10)
            my_entries.append(my_entry)
            

        labelResult = tk.Label(root, bg="#7ca2a2")

        call_result2 = partial(callresult2, labelResult, number5, number6)
        buttonCal2 = tk.Button(root, text="Calculate", command=call_result2, bg="#fd9014")
        buttonCal2.pack()
        labelResult.pack(pady=5)
        #DeleteButton2 = Button(root, text="Delete Text", command=Delete_NonInverting)
        #DeleteButton2.pack(pady=10)


#
# def selected(event):
#     myLabel = Label(root, text=clicked.get()).pack()
#
#     if clicked.get() == "Inverting Op-Amp":
#
#         # Inverting Amp
#         labelNum1 = tk.Label(root, text="Enter Feedback Resistor", bg="#808080").pack()
#         entryNum1 = tk.Entry(root, textvariable=number1).pack()
#         labelNum2 = tk.Label(root, text="Enter Ground Resistor", bg="#808080").pack()
#         entryNum2 = tk.Entry(root, textvariable=number2).pack()
#         labelGain = tk.Label(root, bg="#7ca2a2")
#         # labelGain.pack()
#
#         call_result = partial(callresult, labelGain, number1, number2)
#         buttonCal = tk.Button(root, text="Calculate", command=call_result, bg="#fd9014").pack()
#         labelGain.pack()
#
#     if clicked.get() == "Non Inverting Op-Amp":
#         # Non Inverting Amp
#         labelNum3 = tk.Label(root, text="Enter Feedback Resistor", bg="#808080").pack()
#         entryNum3 = tk.Entry(root, textvariable=number3).pack()
#         labelNum4 = tk.Label(root, text="Enter Ground Resistor", bg="#808080").pack()
#         entryNum4 = tk.Entry(root, textvariable=number4).pack()
#         labelGain1 = tk.Label(root, bg="#7ca2a2")
#         # labelGain.pack()
#
#         call_result1 = partial(callresult1, labelGain1, number3, number4)
#         buttonCal1 = tk.Button(root, text="Calculate", command=call_result1, bg="#fd9014").pack()
#         labelGain1.pack()


# Drop down menu
options = [
    "Inverting Op-Amp",
    "Non Inverting Op-Amp",
    "Resistors in Parallel",
]

# Combo Box
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
labelTitle = tk.Label(root, text="Welcome to Electronics Calculator", bg="#808080", font=fontStyle).pack(pady=10)
labelSubtitle = tk.Label(root, text="Options:", bg="#808080", font=fontStyle1).pack(pady=10)
myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboClick)
myCombo.pack(pady=10)

root.mainloop()