# Generated by Django 3.1.5 on 2021-01-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_donor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(max_length=3),
        ),
    ]
