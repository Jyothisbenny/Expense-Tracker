# Generated by Django 3.1.5 on 2021-02-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210202_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.IntegerField(),
        ),
    ]