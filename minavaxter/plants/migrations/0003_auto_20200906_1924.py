# Generated by Django 3.0.3 on 2020-09-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20200729_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image_profile',
            options={'ordering': ('date_create', 'plant')},
        ),
        migrations.AlterField(
            model_name='image_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='plants/'),
        ),
    ]
