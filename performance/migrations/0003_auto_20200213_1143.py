# Generated by Django 3.0.3 on 2020-02-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20200213_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='performance.Author'),
        ),
    ]
