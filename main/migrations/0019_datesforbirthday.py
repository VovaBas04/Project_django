# Generated by Django 4.0.6 on 2022-08-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_notes_hour_notes_lec_alter_notes_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatesForBirthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_b', models.DateField(null=True, verbose_name='За сколько?')),
            ],
        ),
    ]
