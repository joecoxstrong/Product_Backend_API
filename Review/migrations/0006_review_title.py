# Generated by Django 4.0.3 on 2022-03-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0005_alter_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
