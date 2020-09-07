# Generated by Django 3.0.3 on 2020-07-15 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantfamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, unique=True)),
                ('species', models.CharField(blank=True, max_length=100)),
                ('light', models.CharField(choices=[('MISSING_DATA', 'Missing Data'), ('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MISSING_DATA', max_length=100)),
                ('light_details', models.TextField(blank=True, max_length=2000)),
                ('water', models.CharField(choices=[('MISSING_DATA', 'Missing Data'), ('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MISSING_DATA', max_length=100)),
                ('water_details', models.TextField(blank=True, max_length=2000)),
                ('info', models.TextField(blank=True, max_length=2000)),
                ('link', models.URLField(max_length=1000)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name', 'date_create'),
            },
        ),
        migrations.CreateModel(
            name='Plantprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watered', models.DateField(blank=True, default='2000-01-01', null=True)),
                ('fertilizer', models.DateField(blank=True, default='2000-01-01', null=True)),
                ('kia', models.BooleanField(default=False)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plantfamily')),
            ],
            options={
                'ordering': ('plant', 'date_create'),
            },
        ),
        migrations.CreateModel(
            name='Image_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='plants/')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plantprofile')),
            ],
            options={
                'ordering': ('-date_create', 'plant'),
            },
        ),
        migrations.CreateModel(
            name='Groth_rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(default=0)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plantprofile')),
            ],
            options={
                'ordering': ('-date_create', 'plant'),
            },
        ),
    ]
