# Generated by Django 3.2.13 on 2022-06-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('nombre', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='nombre')),
                ('email', models.CharField(max_length=10, verbose_name='email')),
                ('contraseña', models.IntegerField(verbose_name='precio')),
            ],
        ),
    ]