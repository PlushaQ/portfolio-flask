from flask import Flask, render_template
from datetime import datetime
from database import db, Project, Photo

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def index():
    projects = Project.query.all()  # Fetch all projects from the database
    return render_template('index.html', projects=projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/socials')
def socials():
    return render_template('socials.html')

@app.route('/projects')
def projects():
    projects = Project.query.all()  # Fetch all projects from the database
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)