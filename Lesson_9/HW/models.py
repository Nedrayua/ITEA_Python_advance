import mongoengine as me

me.connect('STUDENTS')


class Faculty(me.Document):
    faculty_name = me.StringField(required=True, min_length=2, max_length=256)
    groups = me.ListField(me.ReferenceField('Group'))

    def __str__(self):
        return f'{self.faculty_name}'

    def view_excellent_students(self):
        excellent_student = f'Факультет: {self.faculty_name}\n'
        number = 1
        for group in self.groups:
            for student in group.students:
                if student.average_mark() >= 4:

                    excellent_student += f'{number}) {student.full_name}, группа: {group.group_name},' \
                                         f' средний балл: {student.average_mark():0.2f}\n'
                    number += 1
        return excellent_student


class Group(me.Document):
    group_name = me.StringField(required=True, min_langth=2, max_length=256)
    faculty = me.ReferenceField(Faculty)
    students = me.ListField(me.ReferenceField('Student'))

    def __str__(self):
        return f'{self.group_name}'

    def add_faculty(self, faculty):
        """
        Назначает группу к факультету и указывает в факультете группу
        """
        self.faculty = faculty
        faculty.groups.append(self)
        self.save()
        faculty.save()


class Curator(me.Document):
    curator_full_name = me.StringField(required=True, min_length=2, max_length=256)
    students = me.ListField(me.ReferenceField('Student'))

    def view_students(self):
        """
        Метод для получения списка студентов по куратору
        """
        list_of_student = ''
        for stud in self.students:
            list_of_student += f'{stud.full_name}, группа: {stud.group.group_name}\n'
        return list_of_student


class LearningSubject(me.Document):
    ls_name = me.StringField(required=True, min_length=2, max_length=256)


class Student(me.Document):
    full_name = me.StringField(required=True, min_length=5, max_length=256)
    grades = me.ListField()
    curator = me.ReferenceField(Curator)
    group = me.ReferenceField(Group)

    def add_grades(self, l_subject, grades):
        """
        Добавляет в оценку в поле grades.
        :l_subject: LearningSubject - экземпляр класса
        :grades: str - оценка
        """
        t_dict = {str(l_subject.ls_name): grades}
        self.grades.append(t_dict)
        self.save()

    def add_group(self, group):
        """
        Привязывает студента к конкретной группе
        """
        self.group = group
        group.students.append(self)
        self.save()
        group.save()

    def add_curator(self, curator):
        """
        Назначает студенту куратора в поле куратор и добавляет куратру студента
        """
        self.curator = curator
        curator.students.append(self)
        self.save()
        curator.save()

    def average_mark(self):
        """
        Определяет среднюю оценку студента
        """
        count = 0
        for g in self.grades:
            for v in g.values():
                count += int(v)
        return count / len(self.grades)

    def view_marks(self):
        """
        Просмотр оценок по студенту
        """
        values = ''
        for value in self.grades:
            for k, v in values.item():
                values += f'{k}: {v}\n'
        return values






