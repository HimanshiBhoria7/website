from django.conf.urls import url,include
from django.contrib import admin
from app11 import views

app_name = 'app11'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^index3/', include('app11.cont')),
    url(r'^$',views.front),
    url(r'^index3', views.index3),
    url(r'^index/', views.index),
    url(r'^home/',views.home),
    url(r'^student3/',views.student3),
    url(r'^student/',views.student),
    url(r'^front3/',views.front3),

]