# Generated by Django 4.2.1 on 2023-06-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registeration_login', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.BooleanField(null=True),
        ),
    ]
