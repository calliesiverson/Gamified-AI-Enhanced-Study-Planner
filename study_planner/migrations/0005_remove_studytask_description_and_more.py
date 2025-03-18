# Generated by Django 5.1.7 on 2025-03-12 20:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_planner', '0004_rename_is_completed_studytask_generated_by_ai_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytask',
            name='description',
        ),
        migrations.RemoveField(
            model_name='studytask',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='studytask',
            name='generated_by_ai',
        ),
        migrations.RemoveField(
            model_name='studytask',
            name='title',
        ),
        migrations.AddField(
            model_name='studytask',
            name='daily_breakdown',
            field=models.TextField(default='No daily breakdown available.'),
        ),
        migrations.AddField(
            model_name='studytask',
            name='goal',
            field=models.TextField(default='No goal provided.'),
        ),
        migrations.AddField(
            model_name='studytask',
            name='progress',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studytask',
            name='recommended_resources',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='studytask',
            name='study_tips',
            field=models.TextField(default='No study tips available.'),
        ),
        migrations.AddField(
            model_name='studytask',
            name='task',
            field=models.CharField(default='No study task available.', max_length=255),
        ),
        migrations.AddField(
            model_name='studytask',
            name='time_commitment',
            field=models.CharField(default='No time commitment specified.', max_length=100),
        ),
        migrations.AddField(
            model_name='studytask',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studytask',
            name='weekly_breakdown',
            field=models.TextField(default='No weekly breakdown available.'),
        ),
        migrations.CreateModel(
            name='UserPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
