# Generated by Django 4.1.5 on 2023-01-26 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='lessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.room'),
        ),
    ]
