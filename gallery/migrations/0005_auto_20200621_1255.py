# Generated by Django 3.0.7 on 2020-06-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.FileField(default='media/Screenshot_from_2020-06-13_19-49-07.png', upload_to=''),
        ),
    ]
