from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_first),
    path('test',views.test,name='test'),
    path('signin', views.signin),
    path('signup', views.signup),
    path('registr',views.registr,name="registr"),
    path('signup/signin', views.return_exit),
    path('user/<int:znak>',views.save_date,name='user_send'),
    # path("my_admin/<int:znak>",views.create_year,name="create"),
    path("my_admin",views.return_admin),
    path("my_admin/document/<int:znak>",views.show_table,name="otchet"),
    path("my_admin/uploads/<slug:data>/<slug:after>", views.upload, name='uploads'),
    path("my_admin/uploads_load/<slug:data>/<slug:after>", views.upload_for_study, name='uploads_for_load'),
    path("my_admin/<int:znak>/save",views.save_birthday,name="birthday"),
    path("signin/<int:id1>/<slug:data1>",views.return_data_table,name='data'),
    path ("my_admin/return/<int:znak>",views.return_admin_page,name='return'),
    path("my_admin/full/<int:znak>", views.full_show_table, name="full"),
    path("my_admin/load/<int:znak>", views.stydy_load, name="load"),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
