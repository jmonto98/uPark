# Generated by Django 5.0.2 on 2024-03-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uparkapp', '0005_pay_cuscod_alter_pay_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=12345, max_length=15),
            preserve_default=False,
        ),
    ]