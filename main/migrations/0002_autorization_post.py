# Generated by Django 4.0.6 on 2022-07-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorization',
            name='post',
            field=models.CharField(choices=[('НК', 'начальник кафедры'), ('ЗК', 'заместитель начальника кафедры'), ('ПР', 'профессор'), ('ДЦ', 'доцент'), ('СП', 'старший преподаватель'), ('ПР', 'преподаватель'), ('ДК', 'докторант'), ('АД', 'адъюнкт'), ('СН', 'старший научный сотрудник'), ('ЗН', 'заместитель начальника факультета'), ('НЛ', 'начальник лаборатории'), ('НО', 'начальник отделения'), ('ИО', 'инженер отделения'), ('ИП', 'инженер-программист отделения'), ('РМ', 'радиомеханик'), ('ЛБ', 'лаборант'), ('ТХ', 'техник')], default='ПР', max_length=2),
        ),
    ]
