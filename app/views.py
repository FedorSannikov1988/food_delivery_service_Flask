from .models import Students, Faculties
from flask import render_template
from config import app


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
