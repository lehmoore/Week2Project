import csv

# with open("imdbtitles.csv", newline= '') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     print(csvreader)

    # for row in csvreader:
    #     if row[0] == "movie" and row[4] >= "2010":
    #         print(row[1])


with open("2015.csv", newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

    for row in csvreader:
        if row[1] == "Western Europe":
            print(row[0], row[7])

input_file = "2015.csv"
output_file = "output.csv"
cols_to_remove = [4]

cols_to_remove = sorted(cols_to_remove, reverse = True)
row_count = 0

with open(input_file, "r") as source:
    reader = csv.reader(source)
    with open(output_file, "w", newline ='') as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            print('\r{0}'.format(row_count), end ='')
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)