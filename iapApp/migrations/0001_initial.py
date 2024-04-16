# Generated by Django 5.0.4 on 2024-04-16 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor_us', models.CharField(max_length=15)),
                ('price', models.TextField()),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iaps', to='iapApp.jogo')),
            ],
        ),
    ]
