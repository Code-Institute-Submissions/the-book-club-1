# Generated by Django 3.0.8 on 2020-08-18 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200818_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_year',
            new_name='publ_year',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image_url',
        ),
    ]