# Generated by Django 2.2.2 on 2020-02-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20200222_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]
