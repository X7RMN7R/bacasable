import csv

with open('export-bi-line-stop.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    with open('output.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        index = 0
        for row in spamreader:
            if index > 0 and len(row) > 10:
                row[10] = "01"
                row[11] = "Conditionnement"

            index += 1
            spamwriter.writerow(row)
