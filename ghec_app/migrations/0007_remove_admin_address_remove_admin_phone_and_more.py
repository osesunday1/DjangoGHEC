# Generated by Django 4.2.2 on 2023-07-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghec_app', '0006_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='address',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='phone',
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount_paid',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]