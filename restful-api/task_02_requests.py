#!/usr/bin/python3
"""
2. Consuming and processing data from an API using Python
"""
import requests
import csv

def fetch_and_print_posts():
    """ fetches all post from JSONPlaceholder """

    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    if res.status_code == 200:
        f_json = res.json()

        for data in f_json:
            print(data['title'])

def fetch_and_save_posts():
    """ fetches all post from JSONPlaceholder an save data """
    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    if res.status_code == 200:
        data = res.json()
        data_to_write = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in data]

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_write)
