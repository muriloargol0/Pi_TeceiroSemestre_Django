# Generated by Django 3.2 on 2021-05-26 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_loan_loan_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='load_date',
            new_name='loan_date',
        ),
    ]