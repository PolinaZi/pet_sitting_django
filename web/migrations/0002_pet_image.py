# Generated by Django 4.1.7 on 2023-02-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pets/'),
        ),
    ]
