# Generated by Django 2.1.4 on 2018-12-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('contact', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('repassword', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
