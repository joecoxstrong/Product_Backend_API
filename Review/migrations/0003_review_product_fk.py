# Generated by Django 4.0.3 on 2022-03-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image_link'),
        ('Review', '0002_review_delete_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product_FK',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
