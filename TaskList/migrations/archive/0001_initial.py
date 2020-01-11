# Generated by Django 2.1.7 on 2020-01-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=100, verbose_name='Zadanie')),
                ('Date', models.DateField(verbose_name='Zadanie')),
                ('AddedBy', models.CharField(max_length=30, verbose_name='Wprowadził')),
                ('DateInserted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
