# Generated by Django 4.2.3 on 2023-07-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackathon_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='background_img_path',
            field=models.ImageField(upload_to='Storage'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_img_path',
            field=models.ImageField(upload_to='Storage'),
        ),
    ]