#!/usr/bin/python3


"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests
import sys


if __name__ == '__main__':
    """python3 -c 'print(__import__("my_module").__doc__)'"""
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/user/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos/" \
        .format(employee_id)

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj:
                                (obj['completed'] is true), todos_info))
    total_completed_tasks = len(task_completed)
    total_tasks = len(todos_info)

    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name,total_completed_tasks,total_tasks))

    [print("\t " + task["title"]) for task in task_completed]
