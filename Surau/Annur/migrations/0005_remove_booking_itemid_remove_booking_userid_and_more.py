# Generated by Django 4.1.4 on 2023-11-07 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Annur', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Itemid',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Userid',
        ),
        migrations.DeleteModel(
            name='CusUsers',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
