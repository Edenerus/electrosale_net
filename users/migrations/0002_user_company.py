# Generated by Django 4.2.1 on 2023-06-03 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_remove_provider_staffs'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='network.provider', verbose_name='Компания'),
        ),
    ]
