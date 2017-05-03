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
select = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

Checkbutton(selectScholar, text = "Kalgren", variable=select[0], onvalue=0).pack()
Checkbutton(selectScholar, text = "Wang Li", variable=select[1], onvalue=1).pack()
Checkbutton(selectScholar, text = "Dong Tonghe", variable=select[2], onvalue=2).pack()
Checkbutton(selectScholar, text = "Chou Fakao", variable=select[3], onvalue=3).pack()
Checkbutton(selectScholar, text = "Li Fangkui", variable=select[4], onvalue=4).pack()
Checkbutton(selectScholar, text = "William Baxter", variable=select[5], onvalue=5).pack()
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

#scholars = {0: 'Kalgren', 1: 'Wang Li', 2: 'Dong Tonghe', 3: 'Chou Fakao', 4: 'Li Fangkui', 5: 'William Baxter'}
'''
Exit the program
'''
def deuces():
	print("Bye!")
	sys.exit(0)

def disp_old_chinese():
	charac = charEntry.get().encode("utf-8")
	if not (charDict.has_key(charac) ):
		showerror("Error!", "Character not found!")
	else:
		for val in select:
			if val.get() == 0:
				kal.config(text=old_chinese_matrix[charDict[charac]][0])
			elif val.get() == 1:
				wang.config(text=old_chinese_matrix[charDict[charac]][1])
			elif val.get() == 2:
				dong.config(text=old_chinese_matrix[charDict[charac]][2])
			elif val.get() == 3:
				chou.config(text=old_chinese_matrix[charDict[charac]][3])
			elif val.get() == 4:
				li.config(text=old_chinese_matrix[charDict[charac]][4])
			elif val.get() == 5:
				will.config(text=old_chinese_matrix[charDict[charac]][5])

def disp_mid_chinese():
	charac = charEntry.get().encode("utf-8")
	if not (charDict.has_key(charac) ):
		showerror("Error!", "Character not found!")
	else:
		for val in select:
			if val.get() == 0:
				kal.config(text=mid_chinese_matrix[charDict[charac]][0])
			elif val.get() == 1:
				wang.config(text=mid_chinese_matrix[charDict[charac]][1])
			elif val.get() == 2:
				dong.config(text=mid_chinese_matrix[charDict[charac]][2])
			elif val.get() == 3:
				chou.config(text=mid_chinese_matrix[charDict[charac]][3])
			elif val.get() == 4:
				li.config(text=mid_chinese_matrix[charDict[charac]][4])
			elif val.get() == 5:
				will.config(text=mid_chinese_matrix[charDict[charac]][5])

Label(inputFrame, text = "Select Search Option").pack()
Button(inputFrame, text = "Search Old Chinese", command = disp_old_chinese).pack(side=LEFT)
Button(inputFrame, text = "Search Middle Chinese", command = disp_mid_chinese).pack(side=RIGHT)
inputFrame.pack()

outputFrame = Frame(bd = 1, relief=SUNKEN)
Label(outputFrame, text = "Kalgren", borderwidth=1, relief=SUNKEN, width = 10).grid(row=0, column=0)
Label(outputFrame, text = "Wang Li", borderwidth=1, relief=SUNKEN, width = 10).grid(row=0, column=1)
Label(outputFrame, text = "Dong Tonghe", borderwidth=1, relief=SUNKEN, width = 15).grid(row=0, column=2)
Label(outputFrame, text = "Chou Fakao", borderwidth=1, relief=SUNKEN, width = 10).grid(row=0, column=3)
Label(outputFrame, text = "Li Fangkui", borderwidth=1, relief=SUNKEN, width = 10).grid(row=0, column=4)
Label(outputFrame, text = "William Baxter", borderwidth=1, relief=SUNKEN, width = 15).grid(row=0, column=5)
kal = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 10)
kal.grid(row=1, column=0)
wang = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 10)
wang.grid(row=1, column=1)
dong = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
dong.grid(row=1, column=2)
chou = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 10)
chou.grid(row=1, column=3)
li = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 10)
li.grid(row=1, column=4)
will = Label(outputFrame, text = "", borderwidth=1, relief=SUNKEN, width = 15)
will.grid(row=1, column=5)
outputFrame.pack(side=TOP)

exit = Button(root, text="Exit", command = deuces, width = 20)
exit.pack(side=BOTTOM)

root.mainloop()
