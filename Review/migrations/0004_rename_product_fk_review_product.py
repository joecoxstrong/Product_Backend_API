# Generated by Django 4.0.3 on 2022-03-16 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0003_review_product_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product_FK',
            new_name='product',
        ),
    ]