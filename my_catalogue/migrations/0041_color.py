# Generated by Django 2.2.13 on 2020-09-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0040_auto_20200921_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_list', models.ManyToManyField(to='catalogue.Product')),
            ],
        ),
    ]