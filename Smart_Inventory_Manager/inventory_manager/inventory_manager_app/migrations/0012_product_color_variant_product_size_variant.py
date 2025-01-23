# Generated by Django 5.1.4 on 2025-01-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager_app', '0011_colorvariant_sizevariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='inventory_manager_app.colorvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='inventory_manager_app.sizevariant'),
        ),
    ]
