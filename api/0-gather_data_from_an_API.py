#!/usr/bin/python3


"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests
import sys


def get_employee_todo_progress(emp_id):
    """python3 -c 'print(__import__("my_module").__doc__)'"""
    api_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        user_data = response.json()

        user_name = user_data['name']

        url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
        response = requests.get(url)
        response.raise_for_status()
        todo_data = response.json()

        comp_tasks = [task for task in todo_data if task['completed']]
        tot_tasks = len(todo_data)
        result  = {len(comp_tasks)}/{tot_tasks}

        print(f"Employee {user_name} is done with tasks ({result}):")
        print(f"{user_name}: {len(comp_tasks)}/{tot_tasks}")

        for task in comp_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <emp_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
