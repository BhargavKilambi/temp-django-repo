from django.conf.urls import url,include
from .views import view_meds,view_list,search

urlpatterns = [
    url(r'home/$',view_meds),
    url(r'list/$',view_list),
    url(r'result/$',search,name='result'),
]
