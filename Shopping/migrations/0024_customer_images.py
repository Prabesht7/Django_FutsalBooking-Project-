# Generated by Django 4.0.3 on 2022-04-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0023_alter_profile_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='images',
            field=models.ImageField(blank=True, default='static/UserProfile/user.png', null=True, upload_to='static/UserProfile'),
        ),
    ]
