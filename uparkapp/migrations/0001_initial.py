# Generated by Django 5.0.2 on 2024-02-26 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('idCard', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idPerson', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField()),
                ('personType', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10)),
                ('idCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uparkapp.card')),
            ],
        ),
    ]
