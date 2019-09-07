import csv 
import os

udemy_csv = os.path.join(".","web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
reviews_percent = []
length = []


with open(udemy_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # test = next(csvreader)

    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent = round(int(row[6]) / int(row[5]), 2)
        reviews_percent.append(percent)
        new_length = row[9].split(" ")
        length.append( float(new_length[0]) )

    cleanCsv = zip(title, price, subscribers, reviews, reviews_percent, length)

    outputFile = os.path.join("webFinal.csv")

    with open(outputFile, "w", newline="\n") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Title", "Course Price", "Subscribers", "Reviews", "Percent of Reviews", "Length of Course"])
        writer.writerows(cleanCsv)

    