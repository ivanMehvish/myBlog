# Generated by Django 5.0.2 on 2024-02-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
