# Generated by Django 4.0.6 on 2022-07-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_notes_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorization',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='autorization',
            name='is_not_print',
            field=models.BooleanField(default=False),
        ),
    ]
