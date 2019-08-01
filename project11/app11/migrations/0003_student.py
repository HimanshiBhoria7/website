# Generated by Django 2.2.3 on 2019-07-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0002_auto_20190726_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerno', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('emailid', models.EmailField(max_length=250, unique=True)),
            ],
        ),
    ]