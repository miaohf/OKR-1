# Generated by Django 2.1.7 on 2019-03-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objective', '0003_auto_20190330_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='correlative_leader',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
