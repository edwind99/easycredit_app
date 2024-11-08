# Generated by Django 5.1.1 on 2024-10-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=127, unique=True)),
                ('first_name', models.CharField(max_length=511)),
                ('last_name', models.CharField(max_length=511)),
            ],
        ),
    ]
