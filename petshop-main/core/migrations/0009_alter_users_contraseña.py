# Generated by Django 3.2.13 on 2022-06-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_users_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='contraseña',
            field=models.CharField(max_length=50, verbose_name='contrasena'),
        ),
    ]
