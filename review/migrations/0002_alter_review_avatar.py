# Generated by Django 5.1.1 on 2024-09-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
