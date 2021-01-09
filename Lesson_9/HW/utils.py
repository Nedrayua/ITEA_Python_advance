import random

from models import Group, Faculty, Student, Curator, LearningSubject
import constance


def group_in_faculty():
    """
    Ведет привязку каждой существующей группы к факультету
    """
    for doc in Group.objects():
        if doc.group_name[:1] in constance.fam:
            doc.add_faculty(Faculty.objects.get(faculty_name=constance.FAM))
        if doc.group_name[:1] in constance.fpm:
            doc.add_faculty(Faculty.objects.get(faculty_name=constance.FPM))
    list_of_group = ""
    for doc in Group.objects():
        list_of_group += f'Группа: {doc.group_name}, факультет: {doc.faculty}\n'

    return list_of_group


def create_groups(count):
    """
    Генерирует группы
    """
    groups = ''
    for i in range(count):
        existing_groups = [f'{group_names}' for group_names in Group.objects()]
        group = Group(group_name=f'{random.choice(constance.TITLE)}-{random.choice(constance.YEAR)}'
                                 f'-{random.choice(constance.NUM)}')

        if group.group_name in existing_groups:
            continue
        else:
            group.save()
            groups += f'{group.group_name}\n'

    return groups


def student_in_group():
    """
    В случайном порядке ведет привязку студента к группе
    """
    for doc in Student.objects():
        doc.add_group(random.choice(Group.objects()))


def curator_of_student():
    """
    В случайном порядке ведет привязку студента к группе
    """
    for doc in Student.objects():
        doc.add_curator(random.choice(Curator.objects()))


def create_students(count):
    """
    Генерирует студентов в колличестве указанном в параметре count
    """
    students = ''
    for i in range(count):
        existing_student = [f'{full_name}' for full_name in Student.objects()]
        student = Student(full_name=f'{random.choice(constance.NAME)} {random.choice(constance.SURNAME)} '
                                    f'{random.choice(constance.PATRONYMIC)}')
        if student.full_name in existing_student:
            continue
        else:
            student.save()
            students += f'{student.full_name}'

    return students


def create_curators(count):
    """
    Генерирует кураторв в случайном порядке
    """
    curators = ''
    for i in range(count):
        existing_curators = [f'{curator_full_name}' for curator_full_name in Curator.objects()]
        curator = Curator(curator_full_name=f'{random.choice(constance.NAME)} {random.choice(constance.SURNAME)} '
                                            f'{random.choice(constance.PATRONYMIC)}')
        if curator.curator_full_name in existing_curators:
            continue
        else:
            curator.save()
            curators += f'{curator.curator_full_name}'

    return curators


def generate_ls_subj():
    for i in constance.L_SUBJ:
        LearningSubject(ls_name=i).save()


def generate_marks(num):
    """
    Выставляет случайный образом выбранные оценки по случайным предметам в колличестве num для ткаждого студента
    в базе
    """
    for stud in Student.objects():
        for i in range(num):
            stud.add_grades(random.choice(LearningSubject.objects()), random.choice(constance.GRADES))


def view_excellent_students_faculty():
    """
    Вывод на экран всех отличников в разрезе факультетов
    """
    result = ''
    for faculty in Faculty.objects():
        result += faculty.view_excellent_students()
    return result

