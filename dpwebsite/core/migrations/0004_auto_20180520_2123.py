# Generated by Django 2.0.5 on 2018-05-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180520_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='CRSE_DESCRIPTION',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='CRSE_PREREQUISITE',
            field=models.TextField(),
        ),
    ]
