# Generated by Django 4.1.4 on 2023-11-07 18:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Annur', '0003_remove_booking_itemid_remove_booking_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusUsers',
            fields=[
                ('Userid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Username', models.TextField(max_length=100)),
                ('Useremail', models.EmailField(max_length=254)),
                ('Userphone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employeeid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Employeename', models.TextField(max_length=100)),
                ('Employeephone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Itemid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Itemname', models.TextField(max_length=100)),
                ('Itemquantity', models.IntegerField()),
                ('Itemdescription', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datebooking', models.DateField()),
                ('Datereturn', models.DateField()),
                ('Itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annur.item')),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]