# there is some code I need in the csv library. give it to me.
import csv

# open the csv file that is at csvs/basic.csv and call it csvfile. open it in read mode.
with open('csvs/basic.csv', 'r') as csvfile:
    # prepare the file to be opened
    our_reader = csv.reader(csvfile)
    # go through the file. get the rows. return it as a list.
    names = [row for row in our_reader]

# print the second item in the names list.
print(names[1][2])

len(names)

# find the length of each first name
for row in names:
    print(len(row[2]))

# find the longest first name
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row[2]
print(longest)

# construct a new list consisting of only the first names we have here.
first_names = [row[2] for row in names]
first_names.reverse()
print(first_names)

new_row = [2,'wayne','graham','meh']
names.append(new_row)
print(names)

a_row = [3,'fox','eliza','SO COOL']
print(names + a_row)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i + 30])
