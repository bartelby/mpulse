# Generated by Django 3.1.2 on 2020-10-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpulseapi', '0004_auto_20201006_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='client_member_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=32),
        ),
    ]