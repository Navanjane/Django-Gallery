# Generated by Django 3.0.7 on 2020-06-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20200625_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
