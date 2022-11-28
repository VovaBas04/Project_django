from django.shortcuts import render,redirect,HttpResponse
from .forms import AuthorizationForm,NotesForm,SignForm,NewNotesForm,DateForNoteForm,DatesForBirthdayForm,Before_and_After
from .models import Autorization,Notes,Date, get_date_for_user,add_week,DatesForBirthday,get_birthdays
from django.core.files.storage import FileSystemStorage
import datetime
from django import forms
from django.db import models
import requests

import requests
from bs4 import BeautifulSoup
# Create your views here.
works=["Учебная работа: ","Учебно-методическая работа: ","Организационно-методическая работа: ","Повышение квалификации: ","Воспитательная работа: ","Контроль качества учебного процесса: ","Научно-методическая и научно-исследовательская работа: "]
def my_first(request):
    if request.method=='POST':
        return render(request, 'main/registration.html')
    else:
        return render(request, 'main/registration.html')
def get_all_users():
    users_form = Autorization.objects.all().values("id","login", "password","is_admin","is_not_print")
    logins = {}
    for el in users_form:
        logins.update({el['login']: [el['password'],el["id"],el["is_admin"],el["is_not_print"]]})
    return logins

def remember_notes(login,date):
    notes=Notes.objects.all()
    user=[]
    for el in notes:
        if el.login==login and el.data==date:
            user=el
            break
    dict={'data_otchet':user.data,'lec':user.lec,'hour':user.hour,}
    return dict
def give_my_list(our_text):
    text_all = []
    len_works = len(works)
    start = our_text.find(works[0]) + len(works[0])
    for i in range(1, len_works):
        finish = our_text.find(works[i])
        text_all.append(our_text[start:finish])
        start = finish + len(works[i])
    text_all.append(our_text[start:])
    return text_all
# "!!!!Исправить тест дату 61"
def give_all(my_login):
    give = ''
    try:
        my_notes = Notes.objects.all().get(login=my_login, data=get_date_for_user()[0][0])
        give = my_notes.text
    except:
        my_notes = Notes()
        try:
            my_notes.data = get_date_for_user()[0][0]
        except:
            my_notes.data=''
        my_notes.login = my_login
        my_notes.text = ''
        for i in range(len(works)):
            my_notes.text += works[i] + ' '
    return [({"text": give_my_list(give)}),my_notes]
#Подумать над всего проведено
def show_and_otchet(data,after='1971-1-1'):
    notes = Notes.objects.order_by('login')
    otchet={}
    logins = get_all_users()
    dont2 = Autorization.objects.all()
    dont = []
    data = datetime.datetime.strptime(data, "%Y-%m-%d")
    after = datetime.datetime.strptime(after, "%Y-%m-%d")
    arr=[]
    i=0
    sum_lec=0
    sum_hour=0
    login_for_full=''
    dict_for_table={}
    for el in dont2:
        if not (el.is_not_print):
            dont.append(el.login)
    for el in notes:
        notes_data=datetime.datetime.strptime(el.data,"%Y-%m-%d")
        if (data == notes_data and after.year==1971) or (after.year!=1971 and notes_data>=data and notes_data<after):
            user = (logins.get(el.login.login))
            dict_for_user={}
            if user != None and not (user[3]):
                arr1 = str(el.text).split('\n')
                if login_for_full != el.login.login:
                    arr = []
                    i = 0
                    sum_lec=el.lec
                    sum_hour=el.hour
                else:
                    sum_lec+=el.lec
                    sum_hour+=el.hour
                login_for_full=el.login.login
                for el3 in arr1:
                    arr.append([el3, ' '])
                for element_works in works:
                    dict_for_user.update({element_works[:len(element_works)-2]:""})
                len_arr = len(arr)
                while i < len_arr:
                    try:
                        works.index(arr[i][0])
                        arr.pop(i)
                        len_arr -= 1
                    except ValueError:
                        bol=0
                        element = arr[i].copy()
                        index_for_full=element[0][0:element[0].find(':')]
                        value_for_full=element[0][element[0].find(':'):]
                        for index_for_element in arr:
                            if index_for_full==index_for_element[1]:
                                index_for_element[0]+=value_for_full[1:]
                                bol=1
                                break
                        if bol==0:
                            arr[i][0] = element[0][element[0].find(':'):]
                            arr[i][1] = element[0][0:element[0].find(':')]
                            try:
                                dict_for_user[arr[i][1]]+=arr[i][0]
                            except KeyError:
                                pass
                            i += 1
                        else:
                            arr.pop(i)
                            len_arr-=1
                for j in range(len(arr)):
                    if arr[j][1] == 'Учебная работа':
                        for element_scientist in arr:
                            if element_scientist[1]==' ':
                                arr.remove(element_scientist)
                        arr.insert(j + 1,
                                   ["Всего проведено часов:" + str(sum_hour) + "(из них лекций:" + str(sum_lec) + ')',
                                    ' '])
                        # arr.insert(j+1,[str(sum_hour), 'Всего проведено часов:'])
                        # arr.insert(j+2, [str(sum_lec), " из них лекций:"])
                        break
                try:
                    dont.remove(el.login.login)
                except ValueError:
                    pass
                dict_for_user.update({"Всего проведено часов":sum_hour})
                dict_for_user.update({"Лекций": sum_lec})
                dict_for_table.update({el.login.login:dict_for_user})
                otchet.update({el.login.login + ":": arr})
    return [otchet,dont]
def support_get_date_for_user():
    date=get_date_for_user()
    if len(date)<1:
        return []
    elem=date.pop(len(date)-1)
    # (str(el.data), el.data.strftime("%d-%m-%Y"))
    if len(date)!=0:
        last_data=(date[0][1])
    else:
        last_data=add_week(elem,7)[1]
    last_data=datetime.date(int(last_data[6:10]),int(last_data[3:5]),int(last_data[0:2]))
    last_data=add_week(last_data)
    date.insert(0,(str(last_data),last_data.strftime("%d-%m-%Y")))
    return date
def create_year():
    year=Date.objects.order_by("-data")
    data=year[0].data
    data2=datetime.date(data.year,data.month,data.day)
    today=datetime.date.today()
    if (today.year+1!=data2.year):
        y=data2.year+1
        while data2.year<y:
            data2=add_week(data2)
            year=Date()
            year.data=data2
            year.save()
def signin(request):
    dict_for_error={'error':False}
    create_year()
    if request.method=='POST':
        form = SignForm(request.POST)
        if form.is_valid():
            login=form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            logins=get_all_users()

            if logins.get(login)!=None and logins.get(login)[0]==password:
                dict_for_error.update({'name': login})
                logins = get_all_users()
                dict_for_error.update({'id': logins.get(login)[1]})
                dict_for_error.update({'list':get_date_for_user()})
                dict_for_error.update({'after_list': support_get_date_for_user()})
                dict_for_error.update({"befor": DatesForBirthday.objects.all()[0].h_b})
                my_login = Autorization.objects.all().get(login=login)
                give=''
                try:
                    dict.update({"data_opt":get_date_for_user()[0][0]})
                    my_notes = Notes.objects.all().get(login=my_login, data=get_date_for_user()[0][0])
                    give=my_notes.text
                except:
                    my_notes = Notes()
                    try:
                        my_notes.data =get_date_for_user()[0][0]
                    except:
                        my_notes.data=''
                    my_notes.login = my_login
                    my_notes.text = ''
                    for i in range(len(works)):
                        my_notes.text += works[i] + ' '
                dict_for_error.update({"text":give_my_list(give)})
                dict_for_error.update({"lec":my_notes.lec})
                dict_for_error.update({"hour": my_notes.hour})
                happy_birthday=get_birthdays()
                if happy_birthday==[]:
                    dict_for_error.update({'happy':["Нет ближайших дней рождения"]})
                else:
                    dict_for_error.update({'happy':happy_birthday})
                if logins.get(login)[2]:
                    dict_for_error.update({'flag': True})
                    return render(request, 'main/Admin.html', dict_for_error)
                else:
                    dict_for_error.update({'flag': False})
                    return render(request,'main/User.html',dict_for_error)
            else:
                dict_for_error['error']=True
        else:
            dict_for_error['error']=True
        return render(request, 'main/registration.html',dict_for_error)
def signup(request):
    dict_for_error = {'error': False}
    if request.method=='POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            logins=get_all_users()
            login=form.cleaned_data.get("login")
            if logins.get(login)==None:
                form.save()
                form = AuthorizationForm()
                context = {
                    'form': form,
                }
                return render(request, 'main/signup.html',dict_for_error)
            else:
                dict_for_error['error']=True
        else:
            dict_for_error['error']=True
        return render(request, 'main/registration.html', dict_for_error)

def return_exit(request):
        dict_for_error={'error':False}
        return render(request,'main/registration.html',dict_for_error)
def registr(response):
    dict={'list1':Autorization}
    return render(response,'main/registr.html',dict)
def save_date(request,znak):
    if request.method=='POST':
        dict={}
        el=None
        form=NewNotesForm(request.POST)
        flag_for_save=True
        if form.is_valid() or not (form.is_valid()):
            form1=Notes()
            logins=Autorization.objects.all()
            form1.data = form.cleaned_data['data2']
            form1.hour=form.cleaned_data['hour']
            form1.lec=form.cleaned_data['lec']
            for el in logins:
                if el.id==znak:
                    dict = {"name": el,'list':get_date_for_user()}
                    dict.update({'after_list': support_get_date_for_user()})
                    form1.login=el
                    break
            forms_form_base = Notes.objects.all()
            flag_for_text=True
            base=None
            form1.text = ''
            flag_hour=False
            flag_lec=False
            len_works = len(works)
            for base in forms_form_base:
                if base.data == form1.data and form1.login==base.login:
                    flag_for_text=False
                    if base.hour!=form1.hour:
                        flag_hour=True
                    base.hour=form1.hour
                    if base.lec!=form1.lec:
                        flag_lec=True
                    base.lec=form1.lec
                    for i in range(len_works):
                        now = form.cleaned_data.get('text' + str(i + 1))
                        if now != None:
                            form1.text = form1.text + works[i] + now + '\n'
                        else:
                            form1.text=form1.text+works[i]+'\n'
                    base.text=form1.text
                    if (flag_lec or flag_hour) and form.cleaned_data.get('text1') ==None:
                        flag_for_save = False
                        dict.update({"flag_for_error":True})
                    else:
                        base.save()
                    break
            if flag_for_text:
                if form1.lec!=0:
                    flag_lec=True
                if form1.hour!=0:
                    flag_hour=True
                if (flag_lec or flag_hour) and form.cleaned_data.get('text1')==None:
                    dict.update({"flag_for_error": True})
                    flag_for_save=False
                for i in range(len_works):
                    now=form.cleaned_data.get('text'+str(i+1))
                    if now!=None:
                        form1.text=form1.text+works[i]+now+'\n'
                    else:
                        form1.text = form1.text + works[i] + '\n'
                if flag_for_save:
                    form1.save()
            dict.update({"id":znak})
            dict.update({"flag_for_save":flag_for_save})
            dict.update({"text":give_my_list(form1.text)})
            dict.update({"data_opt":form1.data})
            dict.update({'lec': form1.lec})
            dict.update({'hour': form1.hour})
            dict.update({"befor": DatesForBirthday.objects.all()[0].h_b})
            if el.is_admin:
                dict.update({'flag': True})
                happy_birthday = get_birthdays()
                if happy_birthday == []:
                    dict.update({'happy': ["Нет ближайших дней рождения"]})
                else:
                    dict.update({'happy': happy_birthday})
                return render(request,"main/Admin.html",dict)
            else:
                dict.update({'flag': False})
                return render(request,"main/User.html",dict)
def return_admin(request):
    dict={'name':'admin'}
    return render(request,'main/Admin.html',dict)
def show_table(request,znak):
    if request.method=='POST':
        form=DateForNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("data")
            main=show_and_otchet(data)
            otchet=main[0]
            dont=main[1]
            print(dont)
            return render(request,'main/otchet.html',{"list":otchet,"no":dont,"uploaded_file_url":True,'id':znak,'data':data,'after':'1971-1-1','flag_for_button':True})
def full_show_table(request,znak):
    if request.method=='POST':
        form=Before_and_After(request.POST)
        if form.is_valid() or not form.is_valid():
            befor=form.cleaned_data.get("data_befor")
            after = form.cleaned_data.get("data_after")
            main=show_and_otchet(befor,after)
            otchet=main[0]
            dont=main[1]
            return render(request, 'main/otchet.html',
                          {"list": otchet, "no": dont, "uploaded_file_url": True, 'id': znak, 'data': befor,'after':after,'flag_for_button':True})
def test(request):
    return render(request,'main/base.html')
#Подумать над text
def save_birthday(request,znak):
    if request.method=='POST':
        # dict = {'name': 'admin',"id":znak}
        # dict.update({'list': get_date_for_user()})
        form=DatesForBirthdayForm(request.POST)
        if form.is_valid():
            birthday=DatesForBirthday.objects.all()[0]
            birthday.h_b=form.cleaned_data['h_b']
            birthday.save()
            # dict.update({"befor":DatesForBirthday.objects.all()[0].h_b})
            # return render(request,'main/Admin.html',dict)
            return return_admin_page(request,znak)
def return_data_table(request,id1,data1):
    my_login=Autorization.objects.all().get(id=id1)
    try:
        my_notes=Notes.objects.all().get(login=my_login,data=data1)
    except:
        my_notes=Notes()
        my_notes.data=data1
        my_notes.login=my_login
        my_notes.text=''
        for i in range(len(works)):
            my_notes.text+=works[i]+' '
    dict={}
    text_all=give_my_list(my_notes.text)
    dict.update({'id': id1})
    dict.update({'list': get_date_for_user()})
    dict.update({'after_list': support_get_date_for_user()})
    dict.update({"befor": DatesForBirthday.objects.all()[0].h_b})
    dict.update({'text':text_all})
    dict.update({'name':my_login.login})
    dict.update({'data_opt':data1})
    dict.update({'lec':my_notes.lec})
    dict.update({'hour':my_notes.hour})
    if my_login.is_admin==True:
        happy_birthday = get_birthdays()
        if happy_birthday == []:
            dict.update({'happy': ["Нет ближайших дней рождения"]})
        else:
            dict.update({'happy': happy_birthday})
        dict.update({'flag': True})
        return render(request,'main/Admin.html',dict)
    else:
        dict.update({'flag': False})
        return render(request, 'main/User.html', dict)
def return_admin_page(request,znak):
    users=Autorization.objects.all().get(id=znak)
    arr=give_all(users)
    my_dict=arr[0]
    my_notes=arr[1]
    try:
        get_data=get_date_for_user()[0][0]
    except:
        get_data=''
    dict={
        'id':znak,
        'list':get_date_for_user(),
        "befor": DatesForBirthday.objects.all()[0].h_b,
        "name":my_notes.login.login,
        "data_opt":get_data,
        "lec":my_notes.lec,
        "hour":my_notes.hour
    }
    dict.update({'after_list': support_get_date_for_user()})
    dict.update(my_dict)
    happy_birthday = get_birthdays()
    if happy_birthday == []:
        dict.update({'happy': ["Нет ближайших дней рождения"]})
    else:
        dict.update({'happy': happy_birthday})
    dict.update({'flag': True})
    return render(request,"main/Admin.html",dict)
def stydy_load(request,znak):
    if request.method=='POST':
        form=Before_and_After(request.POST)
        if form.is_valid():
            data=form.cleaned_data.get('data_befor')
            data_for_print=data
            after=form.cleaned_data.get('data_after')
            data_for_after=after
            data = datetime.datetime.strptime(data, "%Y-%m-%d")
            after=datetime.datetime.strptime(after,"%Y-%m-%d")
            notes=Notes.objects.all().order_by('login')
            sum_lec=0
            dont2=Autorization.objects.all()
            dont=[]
            for el in dont2:
                if not (el.is_not_print):
                    dont.append(el.login)
            sum_hour=0
            login_for_full=''
            otchet={}
            for el in notes:
                notes_data = datetime.datetime.strptime(el.data, "%Y-%m-%d")
                if ((data == notes_data and after.year==1971) or (after.year != 1971 and notes_data >= data and notes_data < after)) and not (el.login.is_not_print):
                    if login_for_full!=el.login.login:
                        if login_for_full!='':
                            arr = [(str(sum_hour), 'Всего проведено часов:'), (str(sum_lec), " из них лекций:")]
                            otchet.update({login_for_full:arr})
                            dont.remove(login_for_full)
                        sum_lec=el.lec
                        login_for_full=el.login.login
                        sum_hour=el.hour
                    else:
                        sum_lec+=el.lec
                        sum_hour+=el.hour
            if login_for_full != '':
                arr = [(str(sum_hour), 'Всего проведено часов:'), (str(sum_lec), " из них лекций:")]
                otchet.update({login_for_full: arr})
                dont.remove(login_for_full)
            return render(request, 'main/otchet.html',
                                  {"list": otchet, "no": dont, "uploaded_file_url": True, 'id': znak, 'data': data_for_print,'after':data_for_after,'flag_for_button':False})
def upload_for_load(data,after):
        data = datetime.datetime.strptime(data, "%Y-%m-%d")
        after = datetime.datetime.strptime(after, "%Y-%m-%d")
        notes = Notes.objects.all().order_by('login')
        sum_lec = 0
        dont2 = Autorization.objects.all()
        dont = []
        for el in dont2:
            if not (el.is_not_print):
                dont.append(el.login)
        sum_hour = 0
        login_for_full = ''
        otchet = {}
        for el in notes:
            notes_data = datetime.datetime.strptime(el.data, "%Y-%m-%d")
            if ((data == notes_data and after.year == 1971) or (
                    after.year != 1971 and notes_data >= data and notes_data < after)) and not (
             el.login.is_not_print):
                if login_for_full != el.login.login:
                    if login_for_full != '':
                        arr = [str(sum_hour), str(sum_lec)]
                        otchet.update({login_for_full: arr})
                        dont.remove(login_for_full)
                    sum_lec = el.lec
                    login_for_full = el.login.login
                    sum_hour = el.hour
                else:
                    sum_lec += el.lec
                    sum_hour += el.hour
        if login_for_full != '':
            arr = [str(sum_hour), (str(sum_lec))]
            otchet.update({login_for_full: arr})
            dont.remove(login_for_full)
        return [otchet,dont]
def razdel(text,dict):
    len_works=len(works)
    start=len(works[0])
    finish=0
    for i in range(1,len_works):
        finish=text.find(works[i])
        if finish-start!=1:
            dict[works[i-1]]+=text[start:finish]
        start=finish+len(works[i])
    dict[works[len_works-1]]+=text[start:]
    return dict
def show_and_otchet_load(data,after='1971-1-1'):
    notes = Notes.objects.order_by('login')
    otchet={}
    logins = get_all_users()
    dont2 = Autorization.objects.all()
    dont = []
    data = datetime.datetime.strptime(data, "%Y-%m-%d")
    after = datetime.datetime.strptime(after, "%Y-%m-%d")
    arr=[]
    i=0
    sum_lec=0
    sum_hour=0
    login_for_full=''
    dict_for_table={}
    dict_for_user={}
    for el in dont2:
        if not (el.is_not_print):
            dont.append(el.login)
    for el in notes:
        notes_data=datetime.datetime.strptime(el.data,"%Y-%m-%d")
        if (data == notes_data and after.year==1971) or (after.year!=1971 and notes_data>=data and notes_data<after):
            user = (logins.get(el.login.login))
            if user != None and not (user[3]):
                if login_for_full != el.login.login:
                    dict_for_user.update({"Всего проведено часов":sum_hour})
                    dict_for_user.update({"из них лекций":sum_lec})
                    if login_for_full!='':
                        dict_for_table.update({login_for_full:list(dict_for_user.values())})
                    dict_for_user={}
                    for elements_works in works:
                        dict_for_user.update({elements_works:' '})
                    sum_lec = el.lec
                    sum_hour = el.hour
                else:
                    sum_lec += el.lec
                    sum_hour += el.hour
                dict_for_user=razdel(el.text,dict_for_user)
                login_for_full = el.login.login
                try:
                    dont.remove(login_for_full)
                except:
                    pass
    dict_for_user.update({"Всего проведено часов": sum_hour})
    dict_for_user.update({"из них лекций": sum_lec})
    dict_for_table.update({login_for_full: list(dict_for_user.values())})
    return [dict_for_table,dont]
def upload_for_study(request,data,after):
   if request.method=='POST':
    content=''
    main=upload_for_load(data,after)
    otchet=main[0]
    dont=main[1]
    # for el in otchet:
    #     content+=el.center(10)
    #     for text in otchet[el]:
    #         content+=text[0].center(30)
    #     content+='\n'
    # content+='\n\n\n'+'Не отчитались\n'
    arr=["Фамилия","Проведено часов","из них лекций"]
    print(arr)
    print(otchet,"Для загрузки")
    return render(request,'main/text.html',{"list":otchet,"flag_for_list":False,"caption":arr,"dont":dont})
def upload(request,data,after):
   if request.method=='POST':
    # content=''.center(10)+'Всего проведено часов'.center(30)+'из них лекций'.center(30)+'\n'
    main=show_and_otchet_load(data,after)
    otchet=main[0]
    print(otchet,"Обычный")
    dont=main[1]
    # for el in dont:
    #     content+=el+'\n'
    arr=works.copy()
    arr.insert(0,"Фамилия")
    arr.append("Проведено часов")
    arr.append("из них лекций")
    print(otchet,arr)
    return render(request,'main/text.html',{"list":otchet,"flag_for_list":False,"caption":arr,"dont":dont})