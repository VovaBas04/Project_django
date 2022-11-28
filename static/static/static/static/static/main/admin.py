from django.contrib import admin
from .models import Autorization,Notes,Date,DatesForBirthday
from django.contrib.auth.models import User


# Обновите поля и сохраните их снова
class AutorizationAdmin(admin.ModelAdmin):
    list_display = ['id','login','name',"dad","birthday",'post',"rank","scientist","degree","is_not_print","is_admin"]
    list_editable= ['login','name',"dad","birthday",'post',"rank","scientist","degree","is_not_print","is_admin"]
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id','login','data','text','hour','lec']
    list_editable= ['login','data','text','hour','lec']
class DateAdmin(admin.ModelAdmin):
    list_display = ['data','archive']
    list_editable = ['archive']
admin.site.register(Autorization,AutorizationAdmin)
admin.site.register(Notes,NotesAdmin)
admin.site.register(Date,DateAdmin)
# admin.site.register(DatesForBirthday)