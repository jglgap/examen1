# Generated by Django 4.2.19 on 2025-02-28 10:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=200)),
                ('numberOfYear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2010), django.core.validators.MinValueValidator(1970)])),
                ('slug', models.SlugField(blank=True)),
                ('finishedDegree', models.BooleanField(default=True)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fkstudents', to='app.degree')),
            ],
        ),
    ]
