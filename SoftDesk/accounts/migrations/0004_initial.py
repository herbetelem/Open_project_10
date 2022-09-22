# Generated by Django 4.0.6 on 2022-08-28 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_delete_usertheme'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('cyborg', 'cyborg'), ('cerulean', 'cerulean'), ('quartz', 'quartz'), ('lumen', 'lumen'), ('simplex', 'simplex'), ('sketchy', 'sketchy')], default='cyborg', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
