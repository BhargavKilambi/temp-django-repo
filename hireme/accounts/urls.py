from django.conf.urls import url,include
from accounts.views import view_list,search,view_home

urlpatterns = [
    url(r'list/$',view_list),
    url(r'home/$',view_home),
    url(r'home/result/$',search,name='result'),
]
