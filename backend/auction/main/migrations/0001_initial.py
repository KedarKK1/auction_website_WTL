# Generated by Django 4.1.7 on 2023-02-27 15:38

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('auction_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('description', models.TextField()),
                ('base_price', models.IntegerField()),
                ('description_brand', models.CharField(max_length=255)),
                ('description_model_number', models.CharField(max_length=255)),
                ('description_date_of_purchase', models.DateTimeField()),
                ('description_location', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
