# Generated by Django 4.0.3 on 2022-04-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infofutsal', '0004_alter_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]
