# Generated by Django 4.2.3 on 2023-07-10 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
