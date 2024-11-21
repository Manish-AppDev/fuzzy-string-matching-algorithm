from rapidfuzz import process, fuzz
import time,csv

def readMyFile(filename):
    data = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[0])
            
    return data

data = readMyFile('Movie.csv')
Src_Str = input("Enter String To Be Searched:")

st = time.time()

def get_matches(query,choices,limit=6):
    results = process.extract(query,choices,scorer=fuzz.WRatio,limit=limit)
    return results
print(get_matches(Src_Str,data))

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

