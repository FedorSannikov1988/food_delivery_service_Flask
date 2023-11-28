from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100),  nullable=False)
    age = db.Column(db.Integer,  nullable=False)
    gender = db.Column(db.Enum('MALE', 'FEMALE'), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.faculty_id'), nullable=False)
    information_about_faculty = db.relationship('Faculties', backref='students')

    def __repr__(self):
        return f'Student({self.id}, {self.name}, {self.surname}, {self.information_about_faculty.title_faculty})'


class Faculties(db.Model):
    faculty_id = db.Column(db.Integer, primary_key=True)
    title_faculty = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'Faculties({self.faculty_id}, {self.title_faculty})'
