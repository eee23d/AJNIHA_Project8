# Generated by Django 3.2.3 on 2021-05-29 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AJNIHA', '0013_delete_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readeraccount',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='readeraccount',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='readeraccount',
            name='country',
        ),
        migrations.RemoveField(
            model_name='readeraccount',
            name='password',
        ),
    ]
