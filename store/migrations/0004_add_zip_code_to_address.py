# Generated by Django 4.1.1 on 2022-09-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
