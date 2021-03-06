# Generated by Django 2.2.5 on 2019-12-06 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('country',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries_states_cities.Country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50)),
                ('country',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries_states_cities.Country')),
                ('state',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries_states_cities.State')),
            ],
        ),
    ]
