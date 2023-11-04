#!/usr/bin/python3

"""
second question
"""
import csv
import sys
import requests

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python 1-export_to_CSV.py <USER_ID>")
    sys.exit(1)

# Define the base URL for the API
base_url = "https://jsonplaceholder.typicode.com"

# Get the USER_ID from the command line argument
user_id = sys.argv[1]

# Send a GET request to the API to retrieve the user's data
response = requests.get(f"{base_url}/users/{user_id}")

if response.status_code != 200:
    print("Error: User not found")
    sys.exit(1)

user_data = response.json()

# Send a GET request to the API to retrieve the user's tasks
tasks_response = requests.get(f"{base_url}/todos?userId={user_id}")
tasks = tasks_response.json()

# Define the CSV filename
csv_filename = f"{user_id}.csv"

# Create and write the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    # Write the task data
    for task in tasks:
        csv_writer.writerow([user_id, user_data['username'], str(task['completed']), task['title'])

print(f"Data exported to {csv_filename}")
