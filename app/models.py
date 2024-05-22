from django.db import models
import json

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    subject = models.CharField(max_length=256)
    days = models.CharField(max_length=512, default=json.dumps({0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}))

    def __str__(self):
        return f"{self.subject}"

    def get_days(self):
        return json.loads(str(self.days))

    def add_days(self, month, days):
        load_days = json.loads(str(self.days))
        for a in days:
            load_days[month].append(a)
        self.days = json.dumps(load_days)
        self.save()


class MarkItem(models.Model):
    mark = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"MarkItem(mark={self.mark}, month={self.month}," \
               f" day={self.day}, subject={self.subject}, student={self.student})"
