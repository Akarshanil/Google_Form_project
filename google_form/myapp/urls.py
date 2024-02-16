from django.urls import path
from . import views


app_name='myapp'

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create,name='create'),
    path('update_form/<str:pk>',views.update_form,name='update_form'),
    path('response/<str:pk>/view_form', views.get_response_from_user, name='view_form'),
    path('forms/<str:pk>/responses', views.responses, name='responses'),

]