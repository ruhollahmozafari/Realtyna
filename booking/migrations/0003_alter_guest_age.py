# Generated by Django 4.1.5 on 2023-01-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_room_lessor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.IntegerField(blank=True, help_text='guest age', null=True),
        ),
    ]
