# Generated by Django 4.0.6 on 2022-08-28 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usertheme_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTheme',
        ),
    ]
