# Generated by Django 4.1.5 on 2023-01-26 15:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='guest name', max_length=20)),
                ('age', models.IntegerField(blank=True, default=20, help_text='guest age', null=True)),
                ('phone_number', models.CharField(help_text='guest phone', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.                                Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(help_text='guest name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='guest name', max_length=20)),
                ('phone_number', models.CharField(help_text='guest phone', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.                                Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(help_text='guest name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ListingOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='listing owner name', max_length=20)),
                ('phone_number', models.CharField(help_text='owner phone', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.                                Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(help_text='owner name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.BigIntegerField(help_text='pay for each night')),
                ('lessor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.room')),
                ('listing_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.listingowner')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('is_checkout', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.guest')),
                ('listing_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.listingowner')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.room')),
            ],
        ),
    ]