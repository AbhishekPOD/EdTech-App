from flask import Flask, request, jsonify
from flask import render_template
from flask import current_app as app
from application.models import *

# db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact-us")
def contact():
    return render_template("contact.html")

@app.route("/grade-<int:grade_name>/subjects")
def show_grade_summary(grade_name):
    grade_subject_objs = Grade_Subject.query.filter_by(grade_name = grade_name).all()
    subject_names = [entry.subject_name for entry in grade_subject_objs]

    subject_objs = [Subject.query.get(subject_name) for subject_name in subject_names]

    return render_template("grade.html", subject_objects = subject_objs, grade_name = grade_name)

@app.route("/grade-<int:grade_name>/subjects/<subject_name>")
def show_subject_summary(grade_name, subject_name):
    subject_obj = Subject.query.get(subject_name)
    all_chapters = Chapter.query.filter_by(subject_name = subject_name).all()
    return render_template("subject_summary.html", all_chapters = all_chapters, subject_obj = subject_obj, grade_name = grade_name)

@app.route("/grade-<int:grade_name>/subjects/<subject_name>/chapter-<int:chapter_number>/")
def show_chapter_details(grade_name, subject_name, chapter_number):
    subject_obj = Subject.query.get(subject_name)
    all_chapter_objs = Chapter.query.filter_by(subject_name = subject_name).all()
    chapter_obj = all_chapter_objs[int(chapter_number)-1]
    return render_template("chapter_details.html", subject_obj = subject_obj, chapter_number = chapter_number, chapter_obj = chapter_obj)

@app.route("/fetch-grades")
def fetch_grades():
    grades = Grade.query.all()
    grade_names = [grade.grade_name for grade in grades]

    return jsonify(grade_names), 200, {'Access-Control-Allow-Origin' : '*'}

@app.route("/fetch-content/<subject_name>/<int:chapter_number>/")
def fetch_content(subject_name, chapter_number):
    all_chapter_objs = Chapter.query.filter_by(subject_name = subject_name).all()
    chapter_obj = all_chapter_objs[int(chapter_number)-1]
    with open("static/subjects/" + subject_name + "/chapter" + str(chapter_number) + ".txt", "r", encoding="utf-8") as f:
        chapter_content = f.read()
    
    return {
        'content' : chapter_content,
    }, 200, {'Access-Control-Allow-Origin' : '*'}

@app.route("/fetch-youtube-link/<subject_name>/<chapter_title>/")
def fetch_youtube_link(subject_name, chapter_title):
    chapter_obj = Chapter.query.filter_by(subject_name = subject_name, chapter_name = chapter_title).first()
    youtube_link = chapter_obj.youtube_link

    return {
        'content' : youtube_link,
    }, 200, {'Access-Control-Allow-Origin' : '*'}

@app.route("/fetch-quiz/<subject_name>/<chapter_title>")
def fetch_questions(subject_name, chapter_title):
    chapter_obj = Chapter.query.filter_by(subject_name = subject_name, chapter_name = chapter_title).first()

    all_questions = Question.query.filter_by(chapter_id = chapter_obj.chapter_id).all()

    questions_to_be_sent = []
    for question in all_questions:
        question_to_be_added = {}
        question_to_be_added.update({"text" : question.question_text})

        all_options = Option.query.filter_by(question_id = question.question_id).all()
        options = []
        correct_answer = ""
        for option in all_options:
            if option.is_correct:
                correct_answer = option.option_name
            options.append(option.option_name)

        question_to_be_added.update({
            "options" : options,
            "correct_answer" : correct_answer
        })
        questions_to_be_sent.append(question_to_be_added)

    return {
        "questions" : questions_to_be_sent
    }, 200, {'Access-Control-Allow-Origin' : '*'}
