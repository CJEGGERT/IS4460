# Generated by Django 5.0.1 on 2024-05-07 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uta_user', '0007_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('uta_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uta_user.utauser')),
            ],
        ),
    ]
