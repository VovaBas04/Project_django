# Generated by Django 4.0.6 on 2022-07-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_notes_data_alter_notes_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='login',
            field=models.CharField(max_length=20, verbose_name='login'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
