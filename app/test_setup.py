from app.models import *
import random


def add_subjects_all():
    for s in ['Математика', 'Физика', 'Химия']:
        Subject.objects.create(subject=s)
    for subject in Subject.objects.all():
        for m in range(9):
            subject.add_days(month=str(m), days=list(set([random.randint(1, 30) for _ in range(6)])).sort())


def add_marks_all():
    for subject in Subject.objects.all():
        for student in Student.objects.all():
            for month in range(9):
                for day in subject.get_days()[str(month)]:
                    MarkItem.objects.create(mark=random.randint(5, 12), month=month, day=day, student=student, subject=subject)
