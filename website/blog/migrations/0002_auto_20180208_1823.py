# Generated by Django 2.0 on 2018-02-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=300, upload_to='', width_field=750),
        ),
    ]