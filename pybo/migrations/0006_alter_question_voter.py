# Generated by Django 4.1.4 on 2023-01-20 06:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
