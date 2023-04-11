from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
# from urls import *
# Create your views here.
# def hello(request):
#     return HttpResponse("Salom Duny!")

# salomlashish
def loginview(request):
    if request.method == "POST":
        user=authenticate(Username=request.POST.get("username"),
                     password=request.POST.get("password"))
        if user is None:
            return redirect('login')
        login(request,user)
        return redirect('bosh_sahifa')
    return(request,"login.html")

# bosh sahifa 
def bosh_sahifa(request):
    return render(request,'bosh_sahifa.html')

# kitoblar
def kitoblar(request):
    soz=request.GET.get("qidirish")
    if soz is None:
        st=Book.objects.all()
    else:
        st=Book.objects.filter(name__contains=soz)|Book.objects.filter(janr__contains=soz)|Book.objects.filter(muallif___contains=soz)
    data={
        # 'forma':KitobForm(),
        'kitoblar':st
    }
    return render(request,"kitoblar.html",data)


# kitob
def kitob_1(request,son):
    if request.method=='POST':
        Book.objects.filter(id=son).update(
            name=request.POST.get('name'),
            muallif_n=request.POST.get('muallif_n'),
            saxifa=request.POST.get("k_s"),
            janr=request.POST.get("janr")
        )
        return redirect('kitob')
    data={
        'kitob':Book.objects.get(id=son)
    }
    return render(request,'kitob.html',data)

# mualliflar
def mualliflar(request):
    if request.method=='POST':
        forma=MuallifForm(request.POST)
        if forma.is_valid():
            Muallif.objects.create(

            )
        return redirect('mualliflar')
    soz=request.GET.get("qidirish")
    if soz is None:
        m_q=Muallif.objects.all()
    else:
        m_q=Muallif.objects.filter(muallif_n__contains=soz)
    data={
        'form':MuallifForm(),
        'mualliflar':m_q,
        'kitoblar':Book.objects.all()
    }
    return render(request,'Mualliflar.html',data)

# muallif
def muallif(request,son):
    if request.method=='POST':
        Muallif.objects.get(id).update(
            muallif_n=request.POST.get('ism'),
            hayot=request.POST.get(''),
            kitoblar=Book.object.get(id=request.POST.get('')),
            jinsi=request.POST.get(''),

        )
    data={
        'muallif':Muallif.objects.get(id=son),
        'kitoblar':Book.objects.all()
    }
    return render(request,'muallif.html',data)

# talabalar
def talabalar(request):
    if request.method=="POST":
        forma=TalabaForm(request.POST)
        if forma.is_valid():
            Student.objects.create(
                name=forma.cleaned_data.get('name'),
                kursi=forma.cleaned_data.get('course'),
                ol_kitob=forma.cleaned_data.get('books'),
                bituruvchi=forma.cleaned_data.get('graduate'),
            )
        return redirect('talabalar')
    data={
        "forms":TalabaForm(),
        'talabalar':Student.objects.all()
    }
    return render(request,'talabalar.html',data)


# talaba
def talaba(request,son):
    if request.method=='POST':
        if request.POST.get('b')=="on":
            bituruvchi=True
        else:
            bituruvchi=False
        Student.objects.filter(id=son).update(
            name=request.POST.get('i'),
            kursi=request.POST.get('k'),
            ol_kitob=request.POST.get("k_s"),
            bituruvchi=bituruvchi
        )
        return redirect('talabalar')
    data={
        'talaba':Student.objects.get(id=son)

    }
    return render(request,'talaba.html',data)


# recordlar
def recordlar(request):
    if request.method=="POST":
        f=RecordForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect('recordlar')
    soz=request.GET.get("qidirish")
    if soz is None:
        RFe=Record.objects.all()
    else:
        RFe=Record.objects.filter(talab_name__name__contains=soz)
    data={
        'forma':RecordForm,
        "recordlar":RFe,
        'talabalar':Student.objects.all(),
        'kitoblar':Book.objects.all()
    }
    return render(request,"recordlar.html",data)


# record
def record(request,son):
    data={
        'record':Record.objects.get(id=son)
    }
    return render(request,'record.html',data)


# talaba ochirish
def talaba_ochir(request,son):
    Student.objects.get(id=son).delete()
    return redirect("/library/talabalar/")


# kitob ochirish
def kitob_ochir(request,son):
    Book.objects.get(id=son).delete()
    return redirect("/library/kitoblar/")


# muallif ochir    
def muallif_ochir(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect("mualliflar")


# record ochir
def record_ochir(request,son):
    Record.objects.get(id=son).delete()
    return redirect("recordlar")

# talaba admin 
def adminlar(request):
    if request.method=='POST':
        admin=AdminForm(request.POST)
        if admin.is_valid():
            admin.save()
        return redirect('adminlar')
    data={
        'adminlar':Admin.objects.all(),
        'admin':AdminForm()
    }
    return render(request,'admin.html',data)

    #admin malumotlari
def Admin_edit(request,son):
    if request.method=="POST":
        Admin.objects.filter(id=son).update(
            name=request.POST.get('ism'),
            ishin_bosh=request.POST.get('ish_bosh'),
            ishin_tush=request.POST.get('ishni_tugashi')
        )
        return redirect('admin')
    data={
        'admin':Admin.objects.get(id=son)
    }
    return render(request,"admin_edit.html",data)
