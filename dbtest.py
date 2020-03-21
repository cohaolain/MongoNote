import pymongo
import time
import random

# Database client
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Load up a list of words (for generating random notes)
with open('words.txt', 'r') as words_file:
    words = words_file.read().splitlines()


class Memo:
    # Constructor for a memo object
    def __init__(self, title, value):
        now = time.time()
        self._data = {
            "title": title,
            "value": value,
            "created_at": now,
            "last_modified": now
        }

    # If you want to update a Memo object later
    def update(self, title="", value=""):
        changeset = {}
        if title:
            changeset.update({"title": title})
        if value:
            changeset.update({"value": value})
        if len(changeset):
            changeset.update({"last_modified": time.time()})
            self._data.update(changeset)

    # Get back the memo as a dict/JSON
    def read(self):
        return self._data

    # Generate a random memo
    def random():
        return Memo(' '.join(random.choices(words, k=random.randint(1, 4))),
                    ' '.join(random.choices(words, k=random.randint(4, 60))))


# Make a sample Memo
test_memo = Memo("Shopping list", "Eggs, bacon & Leberkäse")
test_memo.update(value="Bacon & Leberkäse")

# This refers to the collection of Memos in the DB
memo_collection = myclient.memo_db.memos

# Insert the sample Memo
memo_collection.insert_one(test_memo.read())

# Make 5000 random memos and add them all to the database
random_notes = [Memo.random().read() for _ in range(5000)]
memo_collection.insert_many(random_notes)
