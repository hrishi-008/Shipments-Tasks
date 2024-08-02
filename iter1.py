# iter1.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/email_scheduler'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    schedule_time = db.Column(db.DateTime, nullable=False)
    recurring = db.Column(db.String(20), nullable=True)
    attachments = db.Column(db.Text, nullable=True)

db.create_all()

@app.route('/')
def index():
    return "Email Scheduler API"

if __name__ == '__main__':
    app.run(debug=True)