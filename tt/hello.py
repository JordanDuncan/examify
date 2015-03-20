import csv
import os
import json

contents = {}

for file in os.listdir('csvtt'):
    if file[-4:] != '.csv':
        continue
    with open('csvtt/'+file, 'r') as infile:
        reader = csv.reader(infile)
        with open('naw.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            for row in reader: 
                thisDict = {}
                thisDict['name'] = row[1]
                thisDict['date'] = row[3]
                thisDict['loc'] = row[5]
                thisDict['start'] = row[4][:5]
                thisDict['end'] = row[4][-5:]
                contents[row[0]] = thisDict


open('exams.json','w').write(json.dumps(contents))

print json.dumps(contents)
print len(contents)