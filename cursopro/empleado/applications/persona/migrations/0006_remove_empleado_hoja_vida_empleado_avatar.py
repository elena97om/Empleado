# Generated by Django 4.0.4 on 2022-04-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name_alter_empleado_hoja_vida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
