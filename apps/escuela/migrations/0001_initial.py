# Generated by Django 4.2.4 on 2023-10-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(blank=True, max_length=300, null=True)),
                ('cant_mesas', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
