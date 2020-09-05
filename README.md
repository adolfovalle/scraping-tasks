# scraping-tasks

This is a set of tasks to perform scraping on different websites, task1 is focused on Instagram, task2 is focused on "elpais.com".

# Installation

This is a Django 3.1 project which was created using a virtual environment.

Use:

```shell
pip3 install -r requirements.txt
```
on the main folder to install dependencies.

Having Django installed it's time to then set up the database and run the server locally using:

```shell
python3 manage.py migrate
python3 manage.py runserver
```

With the server running (by default at http://127.0.0.1:8000/) you can now access the urls to trigger the tasks:

http://127.0.0.1:8000/task1

and

http://127.0.0.1:8000/task2

# Setting up Task 1

To set up the input for this task, go to the file "task1/views.py" and add to the variable "lista_usernames" the list of Instagram usernames whose profiles you desire to perform the scraping on.

When you execute this task it will download all the media files (images and videos) for all profiles of this given username list. 

Additionally it will download the metadata (profile username, userid, number of followers, number of followees, and post id, date, caption, along with the number of likes, comments and views) for all these posts into the SQLite database created by Django (db.sqlite3).

Note: The profiles have to be public for the scraping to work properly.

TODO:
- [ ] Make the request asynchronous, so the browser doesn't freeze waiting for completion.
- [ ] Frontend input for username list.

# Setting up Task 2

Task 2 executes scraping on the website "elpais.com" (spanish), it's supposed to obtain data from all video articles on the cover page (Article URL, title, text, and publish date), and save it into the SQLite database, it does not require input.

TODO:
- [x] Make BeautifulSoup recognize more than one video article on the page.
- [x] Download the video file for all articles.
- [ ] Format the date properly (currently handled as text).
