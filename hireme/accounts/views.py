from django.shortcuts import render
from accounts.models import Profile,Category
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
# Create your views here.

def view_home(request):
    items = Profile.objects.all()
    args = {'item':items}
    return render(request,'accounts/home.html',args)

def view_list(request):
    prof = Profile.objects.all()
    return render(request,'accounts/list.html',{'prof':prof})

def search(request):
    query = request.GET.get("q")
    if query:
        items = Profile.objects.filter(Q(name__icontains=query)|Q(category__c_name__icontains=query)|Q(qualification__icontains=query)|Q(des__icontains=query)).distinct()

    return render(request,'accounts/home.html',{'items':items})
