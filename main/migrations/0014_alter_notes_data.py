# Generated by Django 4.0.6 on 2022-07-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_notes_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.CharField(choices=[('2022-05-02', '2022-05-02'), ('2022-07-04', '2022-07-04')], max_length=50, null=True, verbose_name='Дата'),
        ),
    ]
