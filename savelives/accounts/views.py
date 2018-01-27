from django.shortcuts import render,redirect
from .models import Medicine,Pharma
from django.db.models import Q
# Create your views here.
def view_meds(request):
    medicine = Medicine.objects.all()
    x = ['1','2','3',]
    args={'medicine':medicine,'x':x}
    return render(request,'accounts/home.html',args)

def view_list(request):
    medicine = Medicine.objects.all()
    args={'medicine':medicine}
    return render(request,'accounts/list.html',args)

def search(request):
    query = request.GET.get("q")
    if query:
        items = Medicine.objects.filter(Q(name__icontains=query)|Q(price__icontains=query)|Q(company=query)).distinct()

    return render(request,'accounts/home.html',{'items':items})
