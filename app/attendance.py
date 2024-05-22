import json
import os


def get_attendance():
    with open(os.path.join('app/attendance.json'), 'r') as f:
        return json.loads(f.read())


def set_attendance(attendance: dict):
    with open(os.path.join('app/attendance.json'), 'w') as f:
        f.write(json.dumps(attendance))


# attendance = {}
# for student in Student.objects.all():
#     attendance.update({student.id: [['' for _ in range(1, 31)], ['' for _ in range(1, 32)],
#                                     ['' for _ in range(1, 31)], ['' for _ in range(1, 32)],
#                                     ['' for _ in range(1, 32)], ['' for _ in range(1, 29)],
#                                     ['' for _ in range(1, 32)], ['' for _ in range(1, 31)],
#                                     ['' for _ in range(1, 32)]]})
# set_attendance(attendance)
