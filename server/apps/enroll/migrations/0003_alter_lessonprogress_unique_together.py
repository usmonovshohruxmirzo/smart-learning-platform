# Generated by Django 5.2 on 2025-07-18 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_enrollment_student'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonprogress',
            unique_together=set(),
        ),
    ]
