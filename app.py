from flask import Flask, render_template
from datetime import datetime
from database.database import db, Project, Photo  # Import the database and models

app = Flask(__name__)

# Configuration for the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

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
    with app.app_context():
        db.create_all()  # Ensure tables are created before starting the app
    app.run(debug=True)
