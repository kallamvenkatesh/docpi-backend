# Generated by Django 4.1.9 on 2023-05-20 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docpi_app', '0002_remove_user_createdon'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
