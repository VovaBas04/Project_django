# Generated by Django 4.0.6 on 2022-12-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_notes_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.CharField(choices=[('2022-12-26', '26-12-2022'), ('2022-12-19', '19-12-2022'), ('2022-12-12', '12-12-2022')], max_length=50, null=True, verbose_name='Дата'),
        ),
    ]
