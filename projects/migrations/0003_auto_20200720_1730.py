# Generated by Django 3.0.6 on 2020-07-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200606_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]
