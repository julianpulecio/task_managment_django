# Generated by Django 4.1 on 2022-12-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2550)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=7)),
            ],
        ),
    ]
