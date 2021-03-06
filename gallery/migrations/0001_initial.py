# Generated by Django 3.0.7 on 2020-06-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paint_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('paint_image', models.FileField(upload_to='')),
                ('published', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
