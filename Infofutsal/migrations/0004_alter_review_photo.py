# Generated by Django 4.0.3 on 2022-04-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infofutsal', '0003_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/reviewphoto/review.jpg', null=True, upload_to='static/images/reviewphoto'),
        ),
    ]