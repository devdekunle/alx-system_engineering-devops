#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    and export to a json file
"""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"

    employees = requests.get('{}/users'.format(url)).json()
    tasks = requests.get('{}/todos'.format(url)).json()

    json_data = {}

    for employee in employees:
        task_data = []
        for task in tasks:
            if employee.get('id') == task.get('userId'):
                task_data.append({
                    'username': employee.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    })
        json_data.update({str(employee.get('id')): task_data})

    output_file = 'todo_all_employees.json'

    with open(output_file, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
