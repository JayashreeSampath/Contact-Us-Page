# Generated by Django 4.0.5 on 2022-07-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Mail', models.EmailField(max_length=200)),
                ('Sub', models.CharField(max_length=200)),
                ('Msg', models.CharField(max_length=1000)),
            ],
        ),
    ]