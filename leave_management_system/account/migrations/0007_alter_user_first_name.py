# Generated by Django 4.0.3 on 2022-03-31 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_from_employeeleave_date_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
