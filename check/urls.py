from django.conf.urls  import url
from . import views


urlpatterns = [
	
    url(r'^start/', views.fourdig),
    url(r'^saveData/$', views.saveData),
    url(r'^cred/$',views.dispCred),
    url(r'^cred/(?P<id>[A-Za-z0-9.,]+)/$',views.dispCred),
]