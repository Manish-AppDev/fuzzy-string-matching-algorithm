from turtle import width
from matplotlib.animation import MovieWriter
from rapidfuzz import process, fuzz
import time,csv,random
import tkinter as tk
from tkinter import *
from tkinter import simpledialog

def readMyFile(filename):
    data = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[0])
            
    return data

data = readMyFile('Movie.csv')

ROOT = tk.Tk()
ROOT.withdraw()
Src_Str = simpledialog.askstring(title="Movie",prompt="Enter Movie Name\t\t\t\t\t")

st = time.time()

def get_matches(query,choices,limit=10):
    results = process.extract(query,choices,scorer=fuzz.WRatio,limit=limit)
    return results

result = get_matches(Src_Str,data)
len_Srch_Str = int(len(Src_Str)/2) + 1
len_res = len(result)
lst_res = []
tmp_res_len = 0
res_len = []
for i in range(len_res):
    tmp_res_len = (len(result[i][0]))
    if  tmp_res_len > len_Srch_Str:
        lst_res.append(list(result[i]))
        res_len.append(tmp_res_len)
        
for i in range(len(lst_res)):
    lst_res[i][2] = res_len[i]
    
lst_res.sort(key=lambda k: (k[1], -k[2]), reverse=True)

et = time.time()
elapsed_time = et - st

top = tk.Tk()
top.title('List of Movies')
listbox = Listbox(top, height = 150, 
                  width = 500, 
                  bg = "white",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "black")
top.geometry("500x250")  
label = Label(top, text = "Execution time: " + str(round(elapsed_time,3))) 

for i in range(len(lst_res)): 
    listbox.insert(i, lst_res[i][0] + " , " + str(round(lst_res[i][1],3)))

exit_button = Button(top, text="Exit", command=top.quit)

label.pack()
exit_button.pack()
listbox.pack()

top.mainloop()
exit(0)
