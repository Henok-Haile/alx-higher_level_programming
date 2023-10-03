#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(argv[1])
    token = argv[2]
    auth_header = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=auth_header)
    print(response.json().get('id'))
