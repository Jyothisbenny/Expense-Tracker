# Generated by Django 3.1.5 on 2021-02-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210202_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
