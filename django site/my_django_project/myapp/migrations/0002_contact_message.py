# Generated by Django 4.2.5 on 2023-09-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
