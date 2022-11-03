# Generated by Django 3.2.13 on 2022-11-03 01:24

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_contury_review_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]