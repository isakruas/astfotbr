# Generated by Django 3.2 on 2021-05-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=200, unique=True)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
