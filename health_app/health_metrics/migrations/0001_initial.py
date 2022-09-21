# Generated by Django 4.1.1 on 2022-09-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(max_length=20)),
                ('pname', models.TextField(max_length=100)),
                ('plast_name', models.TextField(max_length=100)),
                ('page', models.IntegerField(max_length=2)),
                ('pweight', models.IntegerField(max_length=5)),
                ('pheart_rate', models.IntegerField()),
                ('pspo2', models.IntegerField()),
                ('pestres', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]