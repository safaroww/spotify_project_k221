# Generated by Django 5.0 on 2023-12-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_artist_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='artist/covers/'),
        ),
    ]
