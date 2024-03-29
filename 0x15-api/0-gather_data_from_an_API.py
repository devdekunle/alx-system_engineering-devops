#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    # api url to get user info and todo list for each user
    url_1 = 'https://jsonplaceholder.typicode.com/users/{}'
    user_url = url_1.format(int(argv[1]))
    url_2 = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
    user_todo_url = url_2.format(int(argv[1]))

    # object created from requests response
    user_response = requests.get(user_url)
    user_todo_response = requests.get(user_todo_url)
    # get json dictionary representation of user details
    user_name = user_response.json().get('name')
    # get json dictionary representation of todo list
    todo_list = user_todo_response.json()

    completed_tasks = 0
    uncompleted_tasks = 0
    for task_status in todo_list:
        if task_status.get('completed') is True:
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
    total_tasks = completed_tasks + uncompleted_tasks
    task_st = '{}/{}'.format(completed_tasks, total_tasks)
    print('Employee {} is done with tasks({}):'.format(user_name, task_st))
    for task in todo_list:
        if task.get('completed') is True:
            print('\t {}'.format(task.get('title')))
