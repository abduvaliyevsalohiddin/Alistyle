# Generated by Django 4.2.7 on 2023-12-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_mahsulot_media_izoh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='rasm',
            field=models.FileField(upload_to='Mahsulot'),
        ),
    ]
