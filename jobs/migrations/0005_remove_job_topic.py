# Generated by Django 3.0.6 on 2020-07-04 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200704_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='topic',
        ),
    ]