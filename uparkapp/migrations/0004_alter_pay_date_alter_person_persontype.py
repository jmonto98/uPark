# Generated by Django 5.0.2 on 2024-03-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uparkapp', '0003_alter_card_idcard_alter_pay_idpay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='date',
            field=models.DateTimeField(max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='personType',
            field=models.CharField(choices=[('A', 'Admin'), ('E', 'Empleado'), ('S', 'Estudiante'), ('G', 'Graduado'), ('V', 'Visitante')], max_length=10),
        ),
    ]
