# Generated by Django 4.0.6 on 2022-07-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_notes_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True, verbose_name='Дата')),
                ('archive', models.BooleanField(default=False, verbose_name='Архив')),
            ],
        ),
    ]