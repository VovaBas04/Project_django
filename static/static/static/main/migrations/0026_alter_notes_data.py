# Generated by Django 4.0.6 on 2022-11-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_notes_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.CharField(choices=[], max_length=50, null=True, verbose_name='Дата'),
        ),
    ]
