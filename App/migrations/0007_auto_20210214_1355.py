# Generated by Django 3.1.3 on 2021-02-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phon1',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phon2',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
