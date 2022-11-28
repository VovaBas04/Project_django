from .models import Autorization,Notes,get_date_for_user,add_week,DatesForBirthday
from django.forms import ModelForm,TextInput,Select,Textarea
from django import forms

# from .src.data_for_us import get_date_for_user
import datetime
class AuthorizationForm(ModelForm):
    class Meta:
        model=Autorization
        fields=['login','password','name','post',"scientist","degree","dad","birthday"]
        widgets={"login":TextInput(attrs={
            "type":"text",
            "name":"login",
            "placeholder":"Введите фамилию",
        }),

            "password": TextInput(attrs={
                "type": "password",
                "name": "password",
                "placeholder": "Введите пароль",
            }),
            "name": TextInput(attrs={
                "type": "text",
                "name": "name",
                "placeholder": "Введите имя",
            }),
            "post": Select(attrs={
                "name": "post",
            }),
            "scientist": Select(attrs={
                "name": "scientist",
            }),
            "degree": Select(attrs={
                "name": "degree",
            }),
            "dad": Select(attrs={
                "name": "dad",
            }),
            "birthday": TextInput(attrs={
                "type": "date",
                "name": "birthday",
            }),
        }
class SignForm(ModelForm):
    class Meta:
        model=Autorization
        fields=['login','password']
        widgets=[{"login":TextInput(attrs={
            "type":"text",
            "name":"login",
            "placeholder":"Введите фамилию",
        }),

            "password": TextInput(attrs={
                "type": "password",
                "name": "password",
                "placeholder": "Введите пароль",
            })}]
class NotesForm(ModelForm):
    class Meta:
        model=Notes
        fields=['data','text']
        widgets={'data':TextInput(attrs={"type":"week",
                                         "name":"data"}),
                 'text':TextInput(attrs={"type":"text"})}


choises_data=get_date_for_user()
class NewNotesForm(forms.Form):
    data2=forms.CharField(widget=Select(attrs={'name':'data2'}),max_length=20)
    hour=forms.IntegerField(widget=TextInput(attrs={'name':'hour'}))
    lec=forms.IntegerField(widget=TextInput(attrs={'name':'lec'}))
    # data = forms.CharField(max_length=20)
    text1=forms.CharField(max_length=50,widget=Textarea(attrs={"name":"text1"}))
    text2 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text2"}))
    text3 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text3"}))
    text4 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text4"}))
    text5 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text5"}))
    text6 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text6"}))
    text7 = forms.CharField(max_length=50, widget=Textarea(attrs={"name": "text7"}))
class DateForNoteForm(forms.Form):
    data=forms.CharField(widget=Select(attrs={'name':'data'}),max_length=20)
class DatesForBirthdayForm(ModelForm):
    class Meta:
        model=DatesForBirthday
        fields=['h_b']
        widgets={'h_b':TextInput(attrs={"name":'h_b'})}
class Before_and_After(forms.Form):
    data_befor=forms.CharField(max_length=50,widget=Textarea(attrs={"name":"data_befor"}))
    data_after=forms.CharField(max_length=50,widget=Textarea(attrs={"name":"data_after"}))
