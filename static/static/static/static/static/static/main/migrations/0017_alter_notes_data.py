# Generated by Django 4.0.6 on 2022-07-31 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_autorization_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.CharField(choices=[('2022-07-18', '2022-07-18'), ('2022-07-25', '2022-07-25')], max_length=50, null=True, verbose_name='Дата'),
        ),
    ]