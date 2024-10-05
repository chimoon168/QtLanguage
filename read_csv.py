import csv
with open ("chi.csv", mode = "r", encoding= "utf-8") as f:
    csvRead = csv.DictReader(f)
    print(csvRead)
    for row in csvRead:
        print(row)