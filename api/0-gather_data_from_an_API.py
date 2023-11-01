#!/usr/bin/python3


"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """python3 -c 'print(__import__("my_module").__doc__)'"""
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        user_data = response.json()

        user_name = user_data['name']

        url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        response = requests.get(url)
        response.raise_for_status()
        todo_data = response.json()

        completed_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)

        print(f"Employee {user_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        print(f"{user_name}: {len(completed_tasks)}/{total_tasks}")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
