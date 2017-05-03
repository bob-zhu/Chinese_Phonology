# -*- coding: utf-8 -*-
import csv
from Tkinter import *
from tkMessageBox import showerror, showinfo

CHARS = 'characters.txt'
OLD_PRON = 'old_pronounciation.txt'
NEW_PRON = 'mid_pronounciation.txt'
'''
REQUIREMENTS:
Query an author & character and return OC & MC
Query multiple authors & character and return OC & MC for all authors
Compare initial and final sound changes for same author
	Entire pronunciation, initial, and final
'''

root = Tk()
root.wm_title("Phonology Database")

inputFrame = Frame(root)

selectChar = Label (inputFrame, relief = SUNKEN)
Label(selectChar, text = "Query Character").pack()
charEntry = Entry(selectChar)
charEntry.pack(side = LEFT)
selectChar.pack(side=LEFT)

selectScholar = Label (inputFrame, relief = SUNKEN)
Label(selectScholar, text = "Select Scholar").pack()
select = IntVar()

Radiobutton(selectScholar, text = "Kalgren", variable=select, value = 0).pack()
Radiobutton(selectScholar, text = "Wang Li", variable=select, value = 1).pack()
Radiobutton(selectScholar, text = "Dong Tonghe", variable=select, value = 2).pack()
Radiobutton(selectScholar, text = "Chou Fakao", variable=select, value = 3).pack()
Radiobutton(selectScholar, text = "Li Fangkui", variable=select, value = 4).pack()
Radiobutton(selectScholar, text = "William Baxter", variable=select, value = 5).pack()
selectScholar.pack(side=LEFT)

char_file = open(CHARS)
count = 0
charDict = {}
for char in char_file:
	charDict[char.strip()] = count
	count += 1
count = 0

with open(OLD_PRON) as f:
    reader = csv.reader(f, delimiter="\t")
    old_chinese_matrix = list(reader)

with open(NEW_PRON) as f:
    reader = csv.reader(f, delimiter="\t")
    mid_chinese_matrix = list(reader)

scholars = {0: 'Kalgren', 1: 'Wang Li', 2: 'Dong Tonghe', 3: 'Chou Fakao', 4: 'Li Fangkui', 5: 'William Baxter'}
'''
Exit the program
'''
def deuces():
	print("Bye!")
	sys.exit(0)

def compare():
    charac = charEntry.get().encode("utf-8")
    if not (charDict.has_key(charac) ):
        showerror("Error!", "Character not found!")
    else:
        selScholar.config(text= "Selected Scholar: " + scholars[select.get()])
        oldPron = old_chinese_matrix[charDict[charac]][select.get()]
        midPron = mid_chinese_matrix[charDict[charac]][select.get()]
        old.config(text=oldPron)
        mid.config(text=midPron)
        if not (oldPron.find('-') == -1 or midPron.find('-') == -1):
            oldInit = oldPron[0: oldPron.find('-')]
            midInit = midPron[0: midPron.find('-')]
            if (oldInit == midInit):
                textColor = "black"
            else:
                textColor = "red"
            oldInitialLabel.config(text=oldInit, fg = textColor)
            midInitialLabel.config(text=midInit, fg = textColor)

            oldFin = oldPron[oldPron.find('-') + 1: len (oldPron)]
            midFin = midPron[midPron.find('-') + 1: len(midPron)]
            if (oldFin == midFin):
                textColor = "black"
            else:
                textColor = "red"
            oldFinalLabel.config(text=oldFin, fg = textColor)
            midFinalLabel.config(text=midFin, fg = textColor)
        else:
            oldInitialLabel.config(text = "N/A", fg = "black")
            midInitialLabel.config(text = "N/A", fg = "black")
            oldFinalLabel.config(text = "N/A", fg = "black")
            midFinalLabel.config(text = "N/A", fg = "black")

Button(inputFrame, text = "Compare Old/Middle Chinese", command = compare).pack(side=RIGHT)
inputFrame.pack()

outputFrame = Frame(bd = 1, relief=SUNKEN)

selFrame = Frame()
selScholar = Label(selFrame, text = "Selected Scholar", borderwidth=1, relief=SUNKEN, width = 30)
selScholar.pack()
selFrame.pack()
Label(outputFrame, text = "Old Chinese").grid(row = 0, column = 1)
Label(outputFrame, text = "Middle Chinese").grid(row = 0, column = 2)
Label(outputFrame, text = "Full Pronounciation").grid(row = 1, column = 0)
old = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
old.grid(row = 1, column = 1)
mid = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
mid.grid(row = 1, column = 2)
Label(outputFrame, text = "Initial").grid(row = 2, column = 0)
oldInitialLabel = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
oldInitialLabel.grid(row = 2, column = 1)
midInitialLabel = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
midInitialLabel.grid(row = 2, column = 2)
Label(outputFrame, text = "Final").grid(row = 3, column = 0)
oldFinalLabel = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
oldFinalLabel.grid(row = 3, column = 1)
midFinalLabel = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
midFinalLabel.grid(row = 3, column = 2)

outputFrame.pack(side=TOP)

exit = Button(root, text="Exit", command = deuces, width = 20)
exit.pack(side=BOTTOM)

root.mainloop()
