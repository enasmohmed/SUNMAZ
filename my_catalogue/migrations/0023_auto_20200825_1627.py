# Generated by Django 2.2.13 on 2020-08-25 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0022_auto_20200825_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_en',
            new_name='name_english',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_en',
            new_name='description_english',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_en',
            new_name='title_english',
        ),
    ]
