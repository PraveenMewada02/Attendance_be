# Generated by Django 5.0.6 on 2024-06-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_details',
            name='garnishment_fees',
        ),
        migrations.RemoveField(
            model_name='employee_details',
            name='number_of_garnishment',
        ),
        migrations.RemoveField(
            model_name='employer_profile',
            name='federal_employer_identification_number',
        ),
        migrations.AddField(
            model_name='employee_details',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_details',
            name='empcode',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
