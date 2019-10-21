# Generated by Django 2.1.5 on 2019-01-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Course Name')),
                ('description', models.TextField(verbose_name='Course Content')),
                ('content', models.TextField(verbose_name='Course Content')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('q_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Question ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'All Question',
            },
        ),
        migrations.CreateModel(
            name='McqQuestionModel',
            fields=[
                ('questionmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courseapp.QuestionModel')),
                ('opt_a', models.CharField(max_length=255, verbose_name='Option A')),
                ('opt_b', models.CharField(max_length=255, verbose_name='Option B')),
                ('opt_c', models.CharField(max_length=255, verbose_name='Option C')),
                ('opt_d', models.CharField(max_length=255, verbose_name='Option D')),
            ],
            options={
                'verbose_name': 'MCQ Question',
                'verbose_name_plural': 'MCQ Questions',
            },
            bases=('courseapp.questionmodel',),
        ),
        migrations.CreateModel(
            name='SubQuestionModel',
            fields=[
                ('questionmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courseapp.QuestionModel')),
            ],
            options={
                'verbose_name': 'Subjective Question',
                'verbose_name_plural': 'Subjective Questions',
            },
            bases=('courseapp.questionmodel',),
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.CourseModel'),
        ),
    ]