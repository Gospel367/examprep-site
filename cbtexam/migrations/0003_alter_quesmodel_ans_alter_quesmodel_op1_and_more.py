# Generated by Django 4.0.2 on 2022-06-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtexam', '0002_subject_subject_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='ans',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op4',
            field=models.CharField(max_length=1000),
        ),
    ]