# 1. https://github.com/rogeriolessp/MyScripts/blob/master/HW%206.py

# 2. importing libraries:

import argparse
import os.path as op
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file")
    parser.add_argument("-d", "--degree", help = "Polynomial degree for linear regression (defaults to 1)")
    args = parser.parse_args()
    return args


f = open("C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data", "r")
for line in f:
    read_f = line.split(" ")
    print (read_f)


# 3. converting a function to make data usable

def convert_type (d_value):  # Case 2: is an empty string, should be ignored
    try:
        return int(d_value)
    except ValueError:
        try:
            return float(d_value)
        except ValueError:
            return d_value

# 4. Preparing headers and cleaning data:
def dict_lines(lines, header = False):
    if header:
        column_tits = lines [0]
        lines = lines [1:]
    else:
        column_tits = list(range(1, len(lines[0]) + 1))

    data_dict = {}
    for idx, column in enumerate(column_tits):
        data_dict[column] = []
        for row in lines:
            data_dict[column] += [row[idx]]
        return data_dict
#TESTS
# 1. using hypothesis test to optmize the bug finding work (pip install hypothesis and it installed well)
def test_mean(xs):
    mean = sum(xs) / len(xs)
    assert min(xs) <= mean(xs) <= max(xs)

# 2. test to verify white spaces using isspace
str = " " # string contains space
if str.isspace() == True:
    print("String contains space")
else:
    print("Does not contain space")
str = "t\r\n"
if str.isspace() == True:
    print("String contains space")
else:
    print("Does not contain space")

# 5. Parsing exercice:
# 6. checking if the filepath exists because I have been having to much throuble with filepaths,
# 7. which cost me the time to finish the homework and learn from it:

path = ("C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data")

isFile = os.path.isfile(path)
print (isFile)

# 8. Since the path is correct let's keep going:

# Open csv file:

import csv
with open('wpbc.data', 'r') as csv_file:e    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[1])

# Using Thibault way of dealing with delimeters
def format_row (row):
    if "," in row:
        row = row
    else:
        # shrinkin multiple space separators into a single one and replacing them
        # by a comma in each row
        row = " ".join(row.split())
        row = row,replace(" ", ",")
    return row

def populate_outer_list ():
    data = open(input_file, 'r')
    my_read_data = data.read()
    my_read_data1 = my_read_data.split('\n')
    outer_list = []
    for row in my_read_data1:
        row = format_row(row)
        row_list = []
        for element in row.split(","):
            new_element = convert_type(element)
            if new_element is not None:
                row_list += [new_element]
        if len(row_list) > 0:
            outer_list += [row_list]
        return outer_list
        

# trying to use the two datasets (data and names)

filenames = ["C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data"]
filenames = ["C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wbpc.names"]

if len(filenames) > 1:
        data = open(filenames[0], 'r')
        names = open(filenames[1], 'r')
else:
    data = open(filenames[0], 'r')
    names = None
my_read_data = data.read()
print(my_read_data)

my_read_dataS = my_read_data.split('\n')

outer_list = []
for row in my_read_dataS:
    row_list = []
    for element in row.split(" "):
        new_element = convert_type(element)
        if new_element is not None:
            row_list.append(new_element)
        print(element, end = "\t")
        print(new_element, type(new_element))
        print(row_list)
    if len(row_list) > 0:
        outer_list += [row_list]
  
# 9. Oppening as csv

import csv
with open('wbpc.names', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f 'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f,'\t{row[0]} list {row[1]}.')
            line_count += 1
print(f'Executed {line_count} lines.')



    #csv_reader = csv.reader(fhandle, delimiter = delimiter)

# 10. Add each line in the file to a list:
    lines = []
    if debug:
        count = 0
    for line in csv_reader:
        if debug:
            if count > 2:
                break
            count += 1
        newline = []
        for value in line:
            newline += [convert_type(value)]

        if len(newline) > 0:
            lines += [newline]
return lines


# 3. data cleaning with pandas
import pandas as pd
import numpy as np

pd.DataFrame
df = pd.DataFrame("C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\\Homework\\Homework week 6\\hwk4_data\\wpbc.data")
df = pd.DataFrame(data = wpbc['data'], columns = wpbc ['feature_names'])

# checking the data for any missing values:
wpbc.isnull().sum()

df.describe()

# Overlaid plots:
sns.pairplot (df[cols], plot_kws = {'alpha': 0.6}, diag_kws = {'bins': 30})



if __name__ == "__main__": 
    main()










