# Generated by Django 4.0.2 on 2022-06-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtexam', '0017_alter_subject_options_alter_subject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]