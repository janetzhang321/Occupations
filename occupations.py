#Janet Zhang and Elina HV
#pd 6

from random import choice, uniform
import csv

myDict = {}


import csv
with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        job = row['Job Class']
        percent = float(row['Percentage'])
        if (job != 'Total'): myDict[job] = percent



#print myDict


def randOcc():
    benchmark = uniform(0, sum(myDict.itervalues())) #random number between 0 and the sum of the values of each key 
    total = 0.0
    for key in myDict:
        total+=myDict[key]
        #print "index:" + str(index) + "total:" + str(total)
        if benchmark < total:
            #print "WINN"
            return key
    return key


print randOcc()
