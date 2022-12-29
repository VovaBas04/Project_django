from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class Date(models.Model):
    data=models.DateField('Дата',null=True)
    archive=models.BooleanField('Архив',default=False)

    def __str__(self):
        return str(self.data)
class Autorization(models.Model):
    post_for_choise=[
        ('НК',"заведующий кафедрой"),
        ('ЗК',"заместитель заведующего кафедрой"),
        ("ПР","профессор"),
        ("ДЦ","доцент"),
        ("СП","старший преподаватель"),
        ("ПР","преподаватель"),
        ("ДК","докторант"),
        ("АД","аспирант"),
        ("СН","старший научный сотрудник"),
        ("НЛ","заведующий лабораторией"),
        ("ИО","инженер"),
        ("ИП","программист"),
        ("ЛБ","лаборант"),
        ("ТХ","техник"),
        ("АС","ассистент"),
        ("СЛ","старший лаборант"),
        ("НУ","научный сотрудник"),
        ("МУ","младший научный сотрудник"),
    ]
    degree_for_choises=[
        ("ктн","ктн"),
        ("дтн", "дтн"),
        ("квн", "квн"),
        ("двн", "двн"),
        ("отс","отсутствует"),
        ("кфм","кфмн"),
        ("дфм","дфмн"),
        ("кэн","кэн"),
        ("дэн","дэн"),
        ("кпн","кпн"),
        ("дпн","дпн"),
    ]
    scientist_for_choises=[
        ("доц","доц"),
        ("про","проф"),
        ("снс","снс"),
        ("отс", "отсутствует")
    ]
    login=models.CharField('Логин',max_length=20)
    name=models.CharField('Имя',max_length=20,null=True)
    dad=models.CharField('Отчество',max_length=20,null=True)
    birthday=models.DateField("День рождения",null=True)
    post=models.CharField("должность",max_length=2,choices=post_for_choise,default='ПР')
    degree=models.CharField("уч.степень",max_length=3,choices=degree_for_choises,default='отс')
    scientist=models.CharField("уч.звание",max_length=3,choices=scientist_for_choises,default='отс')
    password=models.CharField('Пароль',max_length=20)
    is_not_print=models.BooleanField("Не выводить",default=False)
    is_admin=models.BooleanField("Админ",default=False)
    def __str__(self):
        return self.login
    def get_absolute_url(self):
        return reverse('signin',kwargs={'znak':self.pk})
def add_week(data,days=7):
    try:
        data = datetime.date(data.year, data.month, data.day + days)
    except ValueError:
        try:
            datetime.date(data.year, data.month,31)
            try:
                data=datetime.date(data.year, data.month+1, days-(31-data.day))
            except ValueError:
                data = datetime.date(data.year+1, 1, days-(31-data.day))
        except ValueError:
            try:
                datetime.date(data.year,data.month,30)
                data = datetime.date(data.year, data.month + 1, days - (30 - data.day))
            except ValueError:
                try:
                    datetime.date(data.year,data.month,29)
                    data = datetime.date(data.year, data.month + 1, days - (29 - data.day))
                except ValueError:
                    data = datetime.date(data.year, data.month + 1, days - (28 - data.day))
    finally:
        return data
def get_date_for_user():
    now=datetime.date.today()
    year = Date.objects.order_by("data")
    arr=[]
    for el in year:
        if now<el.data:
            break
        if not (el.archive):
            arr.append((str(el.data),el.data.strftime("%d-%m-%Y")))
    arr.reverse()
    return arr
class Notes(models.Model):
    login=models.ForeignKey(Autorization,on_delete=models.CASCADE)
    # login=models.CharField("Логин",max_length=50)
    data = models.CharField('Дата',null=True,choices=get_date_for_user(),max_length=50)
    hour=models.IntegerField('Всего',default=0)
    lec=models.IntegerField('Лекции',default=0)
    text=models.TextField('Текст',null=True)
    def __str__(self):
        return self.data
class DatesForBirthday(models.Model):
    h_b=models.IntegerField('За сколько?',null=True)

    def __str__(self):
        return str(self.h_b)
def get_birthdays():
    day_before=DatesForBirthday.objects.all()[0].h_b
    now=datetime.date.today()
    dates_birthday_query=Autorization.objects.all()
    happy=[]
    for val in dates_birthday_query:
        now=datetime.date(val.birthday.year,now.month,now.day)
        delta=val.birthday-now
        delta=delta.days
        if ((delta>=0 and delta<=day_before) or delta+365<=day_before) or (delta<=0 and -delta<=day_before) or delta-365>=-day_before:
            happy.append(str(val.login+' '+val.name+' '+val.dad+'-'+str(val.birthday)))
    return happy
