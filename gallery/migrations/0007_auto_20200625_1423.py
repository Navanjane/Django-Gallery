# Generated by Django 3.0.7 on 2020-06-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
