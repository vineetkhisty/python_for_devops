import requests # Importing the requests library to handle HTTP requests
import json

def get_verse(book,chapter,verse):
    API_URL= "https://bible-api.com/"

    query = f"{book}%20{chapter}:{verse}"

    bible_verse= requests.get(url=f"{API_URL}{query}")

    return bible_verse

book =input("Enter the book from the Bible: ")
chapter= int(input("Enter the chapter number: "))
verse = int(input("Enter the verse to be searched: "))

bible_verse=get_verse(book,chapter,verse)

ref = bible_verse.json()["reference"]
value = bible_verse.json()["text"]

final_value = f"{ref} -- {value}"

try:
    with open("bible_verse.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(final_value) + "\n")
except (IOError, TypeError) as e:
    print("Failed to save JSON:", e)

