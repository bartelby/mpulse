# Code adapted from the internet:
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/

import sys
import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

    # create a list
    data = []

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for row in csvReader:
            data.append(row)

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Driver Code

# Decide the two file paths according to your
# computer system
#csvFilePath = r'Names.csv'
#jsonFilePath = r'Names.json'

# first argument is the name of the input csv file
# second argument is the name of the json file
if __name__ == "__main__":

    # Call the make_json function
    make_json(sys.argv[1], sys.argv[2])

