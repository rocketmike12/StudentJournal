from django.shortcuts import render, redirect
from .models import *
from .forms import MarkForm
from django.http import HttpResponseRedirect
from .attendance import *
import math

# Create your views here.


def index(request):
    return render(request, 'index.html')


def attendance(request):
    if request.method == 'GET':
        calendar_list = [list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 32)), list(range(1, 29)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32))]

        students = Student.objects.all()

        _attendance = get_attendance()

        for student in students:
            if not str(student.id) in _attendance.keys():
                _attendance.update({str(student.id): [['' for _ in range(1, 31)], ['' for _ in range(1, 32)],
                                                      ['' for _ in range(1, 31)], ['' for _ in range(1, 32)],
                                                      ['' for _ in range(1, 32)], ['' for _ in range(1, 29)],
                                                      ['' for _ in range(1, 32)], ['' for _ in range(1, 31)],
                                                      ['' for _ in range(1, 32)]]})

                set_attendance(_attendance)
        for student in students:
            student.attendance = get_attendance()[str(student.id)]

        context = {
            'calendar': calendar_list,
            'students': students,
        }
        return render(request, 'attendance.html', context=context)
    elif request.method == 'POST':
        month = request.POST['month']
        day = request.POST['day']
        student = request.POST['student']
        tick = request.POST['tick']
        _attendance = get_attendance()
        _attendance[student][int(month)][int(day) - 1] = tick
        set_attendance(_attendance)

        return HttpResponseRedirect(request.path_info)


def get_month(request, month):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        for subject in subjects:
            subject.days = subject.get_days()[f"{month}"]

            subject.students = []
            for idx, student in enumerate(Student.objects.all()):
                student.marks = []
                student.idx = idx + 1
                for day in subject.days:
                    try:
                        student.marks.append(
                            MarkItem.objects.filter(month=month, student=student, subject=subject, day=day)[0])
                    except IndexError:
                        student.marks.append(" ")
                subject.students.append(student)

        form = MarkForm()
        form.fields['mark'].label = 'Оценка'
        form.fields['day'].label = 'День'
        form.fields['subject'].label = 'Предмет'
        form.fields['student'].label = 'Студент'

        context = {
            'subjects': subjects,
            'month': month,
            'form': form
        }
        return render(request, 'month.html', context=context)
    elif request.method == 'POST':
        form = MarkForm(request.POST)

        if form.is_valid():
            MarkItem.objects.create(mark=form.cleaned_data['mark'],
                                    month=month,
                                    day=form.cleaned_data['day'],
                                    subject=form.cleaned_data['subject'],
                                    student=form.cleaned_data['student'])

        return HttpResponseRedirect(request.path_info)


def september(request):
    return get_month(request, month=0)


def october(request):
    return get_month(request, month=1)


def november(request):
    return get_month(request, month=2)


def december(request):
    return get_month(request, month=3)


def january(request):
    return get_month(request, month=4)


def february(request):
    return get_month(request, month=5)


def march(request):
    return get_month(request, month=6)


def april(request):
    return get_month(request, month=7)


def may(request):
    return get_month(request, month=8)


def success(request):
    if request.method == 'GET':
        students = Student.objects.all()
        subjects = Subject.objects.all()

        context = {
            'students': students,
            'subjects': subjects
        }
        return render(request, 'success.html', context=context)
    elif request.method == 'POST':
        students = Student.objects.all()
        subjects = Subject.objects.all()

        target_student_id = request.POST['student']
        target_subject_id = request.POST['subject']

        target_student = Student.objects.filter(id=target_student_id)[0]
        target_subject = Subject.objects.filter(id=target_subject_id)[0]
        target_student.marks = []
        for month in range(0, 9):
            monthly_marks = [int(m.mark) for m in MarkItem.objects.filter(month=month, student=target_student, subject=target_subject)]
            try:
                monthly_mark = sum(monthly_marks)/(len(monthly_marks))
            except ZeroDivisionError:
                monthly_mark = 0
            target_student.marks.append(monthly_mark)

        context = {
            'students': students,
            'target_student': target_student,
            'subjects': subjects
        }
        return render(request, 'success.html', context=context)
