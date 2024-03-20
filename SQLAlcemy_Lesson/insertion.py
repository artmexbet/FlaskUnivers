from data import database
from data.__all_models import *

# Инициализируем базу данных
database.init()

# Создаем сессию
session = database.create_session()

# Создаем тестовые данные
subjects = ["Математика", "Физика", "Химия"]
students = ["Иван", "Петр", "Анна"]
teachers = ["Мария", "Алексей", "Елена"]
homeworks = ["Домашнее задание 1", "Домашнее задание 2", "Домашнее задание 3"]
answers = ["Ответ 1", "Ответ 2", "Ответ 3"]

# Добавляем предметы
for title in subjects:
    subject = Subject(title=title)
    session.add(subject)

# Добавляем студентов
for name in students:
    student = Student(name=name, stage=1)
    session.add(student)

# Добавляем учителей
for name in teachers:
    teacher = Teacher(name=name, subject_id=1)
    session.add(teacher)

# Добавляем домашние задания
for description in homeworks:
    homework = Homework(date="2022-01-01", description=description, teacher_id=1)
    session.add(homework)

# Добавляем ответы
for answer in answers:
    answer = Answer(student_id=1, homework_id=1, answer=answer)
    session.add(answer)

# Сохраняем изменения
session.commit()
