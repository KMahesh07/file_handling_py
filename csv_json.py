import csv
import json
import os

def csv_to_json(directory):
    # Create an empty dictionary to store CSV data
    csv_data = {}

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Create the file path
            file_path = os.path.join(directory, filename)
            # Open the CSV file
            with open(file_path, 'r') as csv_file:
                # Read CSV data as a dictionary
                csv_reader = csv.DictReader(csv_file)
                # Create a list to store rows of CSV data
                data = []
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    # Append each row to the data list
                    data.append(row)
                # Add the data list to the dictionary with the filename as key
                csv_data[filename] = data

    # Convert the dictionary to JSON format
    json_data = json.dumps(csv_data, indent=4)

    # Print JSON data
    print(json_data)

    # Write JSON data to a file (optional)
    with open('output.json', 'w') as json_file:
        json_file.write(json_data)

# Specify the directory containing CSV files
directory = 'F:\\Mahesh_k\\csv'

# Convert CSV files to JSON and print the JSON data
csv_to_json(directory)
