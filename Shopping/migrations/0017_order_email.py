# Generated by Django 4.0.1 on 2022-03-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0016_rename_name_order_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
