from .database import db

class Grade(db.Model):
    __tablename__ = 'grade'
    grade_name = db.Column(db.Integer, primary_key=True)
    subjects = db.relationship("Subject", secondary="grade_subject")

class Subject(db.Model):
    __tablename__ = 'subject'
    subject_name = db.Column(db.String, primary_key=True)
    number_of_chapters = db.Column(db.Integer)
    description = db.Column(db.String)
    image_link = db.Column(db.String)

class Grade_Subject(db.Model):
    __tablename__ = 'grade_subject'
    grade_name = db.Column(db.Integer, db.ForeignKey("grade.grade_name"), primary_key=True)
    subject_name = db.Column(db.String, db.ForeignKey("subject.subject_name"), primary_key=True)

class Chapter(db.Model):
    __tablename__ = 'chapter'
    chapter_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    subject_name = db.Column(db.String, db.ForeignKey("subject.subject_name"), nullable=False)
    chapter_name = db.Column(db.String)
    chapter_author = db.Column(db.String)
    youtube_link = db.Column(db.String)
    questions = db.relationship("Question")

class Question(db.Model):
    __tablename__ = 'question'
    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapter.chapter_id"), nullable=False)
    question_text = db.Column(db.String)
    options = db.relationship("Option")

class Option(db.Model):
    __tablename__ = 'option'
    option_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.question_id"), nullable=False)
    option_name = db.Column(db.String)
    is_correct = db.Column(db.Boolean, default = False)

# class User(db.Model):
#     __tablename__ = 'user'
#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     username = db.Column(db.String, unique=True)
#     email = db.Column(db.String, unique=True)

# class Article(db.Model):
#     __tablename__ = 'article'
#     article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String)
#     content = db.Column(db.String)
#     authors = db.relationship("User", secondary="article_authors")

# class ArticleAuthors(db.Model):
#     __tablename__ = 'article_authors'
#     user_id = db.Column(db.Integer,   db.ForeignKey("user.user_id"), primary_key=True, nullable=False)
#     article_id = db.Column(db.Integer,  db.ForeignKey("article.article_id"), primary_key=True, nullable=False) 