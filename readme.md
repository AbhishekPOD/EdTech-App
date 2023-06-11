## B2C Ed-Tech App

An EdTech web app to provide and teach contents to kids in a fun and engaging way. The app consists of lessons, videos, images, and quizzes for the kids to learn themselves and enjoy the learning.

Live Application Link: [abhishekpod.pythonanywhere.com/](http://abhishekpod.pythonanywhere.com/)

## How to run the app:

1. Clone the Github repository using the command below:
```
git clone https://github.com/AbhishekPOD/EdTech-App.git
```

2. Install all the Python depencies in the current environment (use virtual environment, if needed). Run the below command to install all the depencies:
```
pip install -r requirements.txt
```

3. Once, the dependencies are successfully installed, run the app using the below command:
```
python main.py
```

## Project Tree

```
Ed-Tech App
|   .gitignore
|   main.py
|   readme.md
|   requirements.txt
|
+---application
|   |   config.py
|   |   controllers.py
|   |   database.py
|   |   models.py
|   |   __init__.py
|   |
|   \---__pycache__
|           config.cpython-39.pyc
|           controllers.cpython-39.pyc
|           database.cpython-39.pyc
|           models.cpython-39.pyc
|           __init__.cpython-39.pyc
|
+---db_directory
|       testdb.sqlite3
|
+---static
|   |   edtech.png
|   |
|   \---subjects
|       |   art.png
|       |   biology.png
|       |   chemistry.png
|       |   cs.png
|       |   english.png
|       |   geography.png
|       |   history.png
|       |   maths.png
|       |   music.png
|       |   physics.png
|       |   psychology.png
|       |   reading.png
|       |   science.png
|       |
|       +---Art
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Biology
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Chemistry
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Computer Science
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---English
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Geography
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---History
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |       chapter3.png
|       |       chapter3.txt
|       |
|       +---Mathematics
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |       chapter3.png
|       |       chapter3.txt
|       |       chapter4.png
|       |       chapter4.txt
|       |
|       +---Music
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Physics
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Psychology
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       +---Reading
|       |       chapter1.png
|       |       chapter1.txt
|       |       chapter2.png
|       |       chapter2.txt
|       |
|       \---Science
|               chapter1.png
|               chapter1.txt
|               chapter2.png
|               chapter2.txt
|
+---templates
|       about.html
|       base.html
|       chapter_details.html
|       contact.html
|       grade.html
|       home.html
|       subject_summary.html
|
\---__pycache__
        main.cpython-39.pyc
```
