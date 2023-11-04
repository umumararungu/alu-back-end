#!/usr/bin/python3
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    with open(str(employee_id) + '.csv', "w") as f:
        [f.write('"' + str(employee_id) + '",' +
                 '"' + employee_username + '",' +
                 '"' + str(task["completed"]) + '",' +
                 '"' + task["title"] + '",' + "\n")
         for task in todo_info]
