# Generated by Django 3.2.9 on 2021-11-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='laptop_store_url',
            field=models.TextField(max_length=45, null=True),
        ),
    ]
