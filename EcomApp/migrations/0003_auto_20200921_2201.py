# Generated by Django 3.1 on 2020-09-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0002_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
