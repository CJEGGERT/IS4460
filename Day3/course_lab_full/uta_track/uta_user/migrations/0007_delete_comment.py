# Generated by Django 5.0.1 on 2024-05-07 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uta_user', '0006_remove_faqmain_faqs_faq_faq_main'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
