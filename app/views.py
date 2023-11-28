from .models import db, Students, Faculties
from flask import render_template
from config import app


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('database has been created')


@app.cli.command("add-students")
def add_students():

    count: int = 5

    for student in range(1, count + 1):
       new_students = Students(name=f'student_name_{student}',
                               surname=f'student_surname_{student}',
                               age=18,
                               gender='MALE',
                               group=student,
                               faculty_id=student)
       db.session.add(new_students)
    db.session.commit()

    for faculty in range(1, count + 1):
        new_faculty = Faculties(title_faculty=f'title_faculty_{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('database is full')


@app.route('/')
def index():

    students = Students.query.all()
    faculty_one = Faculties.query.get(1)

    context = {
        'title_pag': 'Вывод информации о студентах',
        'students': students,
        'faculty_one': faculty_one
    }
    return render_template('practica_3_task_1_all_students.html', **context)


if __name__ == '__main__':
    app.run()
