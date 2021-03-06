# Generated by Django 2.0.1 on 2018-05-26 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=50)),
                ('edad_años', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CitasAnimales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipodecita', models.CharField(max_length=50)),
                ('motivo', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NombreAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NombreDueño',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dueño', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='historial',
            name='Dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.NombreDueño'),
        ),
        migrations.AddField(
            model_name='historial',
            name='nombreMascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.Caracteristica'),
        ),
        migrations.AddField(
            model_name='citasanimales',
            name='Dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.NombreDueño'),
        ),
        migrations.AddField(
            model_name='citasanimales',
            name='nombreMascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.Caracteristica'),
        ),
        migrations.AddField(
            model_name='citasanimales',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.Raza'),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='Dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.NombreDueño'),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.Raza'),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='tipoAnimal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicinas.NombreAnimal'),
        ),
    ]
