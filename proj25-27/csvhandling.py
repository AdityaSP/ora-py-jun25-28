import csv

# fh = open('data.csv')
# for line in csv.reader(fh):
#     print line
# fh.close()

with open('data.csv') as fh:
    for line in csv.reader(fh):
        print line
