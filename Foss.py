# ///THIS IS NOT A FINAL COPY///

# This program seeks to take an compiled ION channel library check list,
# and compare it to libraries used in individual teams, and separate out the ION channel information,
# into separate library documents associated with each library name

import json

# At the moment the user will have to specify the file path to the ION channel library report

file_path = input("Enter the Ion Channel library JSON Document File Path:  ")

# User will then specify the individual project JSON document that lists what libraries they use and that they wish to
# check against the ION channel report
file_path2 = input("/n Enter the Individual Project library json File Path:  ")

# Users are then asked to include the specific Project name, as this will be the file name that has a list of
# libraries and their output from ION channel
project_name = input("/n Enter the Name of the Project that you want to compile libraries for: ")

# open the file and parse objects

with open(file_path, mode='r') as ion_foss:
    ion_data = json.loads(ion_foss)

# Read ION Channel json file and store content in dictionary ion_foss

# By using json.loads() function

# Open individual team Library comparison file

with open(file_path2, mode='r') as indiv_foss:
    indiv_data = json.loads(indiv_foss)

# This FOR loop seeks to compare the VALUE of "Library" in each document
# if the ION channel report has a "Library" that is also located in the individual project,
# we seek to have the "Library and its information printed into a separate report for that individual program

for value in ion_data.keys['library']:
    if ion_data.value == indiv_data.value['library']:
        print(json.dumps(ion_data, indent=4, sort_keys=True), file=project_name)





