# Generated by Django 5.0.6 on 2024-06-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='id',
        ),
        migrations.AlterField(
            model_name='airport',
            name='airport_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
