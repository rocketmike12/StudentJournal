# Generated by Django 4.2 on 2024-05-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_markitem_student_alter_markitem_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='days',
            field=models.CharField(default='{}', max_length=512),
        ),
    ]