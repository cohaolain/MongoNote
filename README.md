# Note-taking with MongoDB

This is (currently) a very rudimentary sample application exploring the use of a MongoDB database for storing notes.

## Prerequisites

You need to have a running MongoDB instance available.

- If you don't have one available and want one for testing, you can run one with Docker:
  - `docker run -d -p 27017:27017 mongo`

You also need the python libraries listed in `requirements.txt`.

- This is easiest to do with `pip`. You can use the following command to install them:
  - `pip3 install -r requirements.txt`

## Running

You can run the script with `python3 dbtest.py`, or alternatively use `python3 -i dbtest.py`, which will allow you to use the python interpreter once the script has finished.

## More information

You can see the entries created by this script by connecting to your DB address with the [MongoDB Compass](https://www.mongodb.com/download-center/compass) UI, or with any MongoDB client.