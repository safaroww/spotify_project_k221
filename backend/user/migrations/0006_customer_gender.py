# Generated by Django 5.0 on 2023-12-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customer_birth_date_alter_customer_followed_artists_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20),
            preserve_default=False,
        ),
    ]
