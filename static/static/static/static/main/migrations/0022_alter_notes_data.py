# Generated by Django 4.0.6 on 2022-08-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_notes_data_alter_notes_hour_alter_notes_lec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.CharField(choices=[('2022-08-08', '08-08-2022'), ('2022-08-01', '01-08-2022')], max_length=50, null=True, verbose_name='Дата'),
        ),
    ]
