from pickle import TRUE
from fuzzywuzzy import fuzz
import csv
import numpy as np
import time

def readMyFile(filename):
    data = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[0])            
    return data

data = readMyFile('Movie.csv')
Str2 = input("Enter String To Be Searched:")
Movie=[[0 for col in range(2)] for row in range(len(data))]

st = time.time()

for i in range(len(data)):
    Str1 = data[i]
    #Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
    #Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower()) # For Incorrect String Good
    #Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
    Token_Set_Ratio = fuzz.token_set_ratio(Str1,Str2) # For Correct String Good
    Movie[i][0] = Str1 
    Movie[i][1] = Token_Set_Ratio
    
Res = sorted(Movie, key = lambda x: x[1], reverse = True)[:6]
print(Res)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
