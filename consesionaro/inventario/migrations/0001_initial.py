# Generated by Django 3.1 on 2020-10-11 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('idvehiculo', models.ForeignKey(db_column='idvehiculo', on_delete=django.db.models.deletion.DO_NOTHING, to='vehiculo.vehiculo')),
            ],
            options={
                'db_table': 'inventario',
            },
        ),
    ]
