# Generated by Django 2.2.1 on 2019-10-08 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_userlogin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='matric_no',
            new_name='user',
        ),
    ]
