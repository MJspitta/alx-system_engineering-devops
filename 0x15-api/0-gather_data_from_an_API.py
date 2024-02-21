#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def fetch_todo():
    """ get data from api and display todo list progress """
    url = "http://jsonplaceholder.typicode.com/users"
    to_do = "http://jsonplaceholder.typicode.com/todos"
    users = requests.get(url)

    for user in users.json():
        if user.get('id') == int(sys.argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break

    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    todos = requests.get(to_do)

    for td in todos.json():
        if td.get('userId') == int(sys.argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if td.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(td.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))

    for tt in TASK_TITLE:
        print("\t{}".format(tt))


if __name__ == "__main__":
    fetch_todo()
