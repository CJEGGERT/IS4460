# Generated by Django 5.0.1 on 2024-05-06 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uta_user', '0005_faqmain_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqmain',
            name='faqs',
        ),
        migrations.AddField(
            model_name='faq',
            name='faq_main',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='uta_user.faqmain'),
            preserve_default=False,
        ),
    ]
