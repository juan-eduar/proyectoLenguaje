# Generated by Django 3.1.5 on 2021-01-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]
