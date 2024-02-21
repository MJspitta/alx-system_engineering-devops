#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


def fetch_todo():
    """ get data from api and display todo list progress """
    url = "http://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user_resp = requests.get(url + "users/{}".format(user_id))
    user = user_resp.json()

    params = {"userId": user_id}
    todos_resp = requests.get(url + "todos", params=params)
    todos = todos_resp.json()
    complete_list = []

    for td in todos:
        if td.get("completed") is True:
            complete_list.append(td.get("title"))
    print ("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                          len(complete_list),
                                                          len(todos)))
    for c in complete_list:
        print("\t{}".format(c))


if __name__ == "__main__":
    fetch_todo()
