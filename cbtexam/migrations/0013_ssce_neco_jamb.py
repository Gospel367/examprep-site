# Generated by Django 4.0.2 on 2022-06-15 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtexam', '0012_alter_scholarshipcomments_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssce_subject_teacher', to=settings.AUTH_USER_MODEL)),
                ('author_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssce_subject_class', to='cbtexam.level')),
                ('author_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssce_subject', to='cbtexam.subject')),
            ],
        ),
        migrations.CreateModel(
            name='NECO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neco_subject_teacher', to=settings.AUTH_USER_MODEL)),
                ('author_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neco_subject_class', to='cbtexam.level')),
                ('author_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neco_subject', to='cbtexam.subject')),
            ],
        ),
        migrations.CreateModel(
            name='JAMB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jamb_subject_teacher', to=settings.AUTH_USER_MODEL)),
                ('author_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jamb_subject_class', to='cbtexam.level')),
                ('author_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jamb_subject', to='cbtexam.subject')),
            ],
        ),
    ]
