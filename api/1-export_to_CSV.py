#!/usr/bin/python3
"""validation"""

import csv
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                        .format(sys.argv[1])).json()
    content = []

    for task in todo:
        content.append([str(sys.argv[1]),
                        user["username"],
                        task["completed"],
                        task["title"]])

    csv_file = "{}.csv".format(sys.argv[1])
    with open(str(sys.argv[1]) + '.csv', "w") as csv_file:
        for item in content:
            csv_file.write('"' + str(sys.argv[1]) + '",' +
                           '"' + item[1] + '",' +
                           '"' + str(item[2]) + '",' +
                           '"' + item[3] + '",' + "\n")
