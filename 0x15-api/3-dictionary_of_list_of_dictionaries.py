#!/usr/bin/python3
""" export all tasks from all employees in JSON format """

import json
import requests


def fetch_data():
    """ get user info and todo list for all """
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    data_export = {}

    for user in users:
        user_id = user["id"]
        todo_response = requests.get(url + f"todos?userId={user_id}")
        todo_list = todo_response.json()
        data_export[user_id] = []
        for todo in todo_list:
            task_info = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
            }
            data_export[user_id].append(task_info)

    return data_export


if __name__ == "__main__":
    data_to_export = fetch_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
