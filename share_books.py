import json
import csv
from files import BOOKS_FILE_PATH
from files import USERS_FILE_PATH
import sys


# Part 1: Creating list of books
books = []
book_count = 0

with open(BOOKS_FILE_PATH) as f:
    reader = csv.DictReader(f)

    for row in reader:
        book = {
            'title': row["Title"],
            'author': row["Author"],
            'pages': row["Pages"],
            'genre': row["Genre"]

        }
        books.insert(book_count, book)
        book_count += 1


# Part 2:  Creating list of users
users = []
users_count = 0

with open(USERS_FILE_PATH) as file:
    users_list = json.load(file)

for val in users_list:
    user = {
     'name': val['name'],
     'gender': val['gender'],
     'address': val['address'],
     'age': val['age'],
     'books': []
    }
    users.insert(users_count, user)
    users_count += 1


# Part 3:  Share books between users. 1 book goes to 1 user, until no books left in the list
index_books = 0
index_users = 0

# while books left in the list
while len(books) > 0:
    if index_users == users_count:
        index_users = 0

    users[index_users]['books'].append(books[0])

    index_users += 1
    books.remove(books[0])


# Write json file with results
with open("result.json", "w") as f:
    content = json.dumps(users, indent=4)
    f.write(content)






