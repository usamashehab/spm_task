# Generated by Django 4.2.11 on 2024-05-02 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='approver',
        ),
    ]