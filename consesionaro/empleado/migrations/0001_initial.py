# Generated by Django 3.1 on 2020-10-11 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('tipodocumento', models.CharField(db_column='tipoDocumento', max_length=100)),
                ('numdocumento', models.IntegerField(db_column='numDocumento')),
                ('horario', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
    ]
