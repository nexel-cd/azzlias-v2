# Generated by Django 5.1.1 on 2024-09-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, related_name='products', to='home.size'),
        ),
    ]
