# Generated by Django 2.1.2 on 2018-11-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0013_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]