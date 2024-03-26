import csv

with open("myCSV.csv") as datafile:
    data = csv.reader(datafile)
    for row in data:
        print(row)