# Generated by Django 5.0.1 on 2024-01-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0002_alter_categories_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
