# Generated by Django 5.0.6 on 2024-06-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('release_year', models.IntegerField(blank=True, max_length=4, null=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, max_length=50, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube_url', models.TextField(blank=True, null=True)),
                ('img_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
