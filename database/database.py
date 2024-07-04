from flask_sqlalchemy import SQLAlchemy

# Initialize the database without an app context
db = SQLAlchemy()

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)
    photos = db.relationship('Photo', backref='project', lazy=True)

    def __repr__(self):
        return f'<Project {self.title}>'

# Define the Photo model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __repr__(self):
        return f'<Photo {self.path}>'
