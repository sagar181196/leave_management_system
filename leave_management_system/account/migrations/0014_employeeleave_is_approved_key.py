# Generated by Django 4.0.3 on 2022-03-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='is_approved_key',
            field=models.BooleanField(default=True, max_length=50),
        ),
    ]
