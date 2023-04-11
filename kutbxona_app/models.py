from django.db import models
from django.db.models import Sum, Max, Min, Avg

# Create your models here.
class Book(models.Model):
    muallif_n=models.CharField(max_length=50,blank=True)
    name=models.CharField(max_length=60,blank=True)
    saxifa=models.SmallIntegerField()
    janr=models.CharField(max_length=20,blank=True)
    def __str__(self) -> str:
        return self.name
class Muallif(models.Model):
    muallif_n=models.CharField(max_length=32)
    hayot=models.BooleanField("hayot",default=True)
    kitoblar=models.ForeignKey(Book,on_delete=models.CASCADE)
    jinsi=models.BooleanField("erkak",default=True)
    tugulan_sana=models.DateField()
    kitoblar_soni=models.SmallIntegerField()
    yosh=models.SmallIntegerField("nechi yoshda vafot etani yoki nechi yosh",)
    def __str__(self) -> str:
        return self.muallif_n
class Student(models.Model):
    k=[
        ("1 kurs","1 kurs"),
        ("2 kurs","2 kurs"),
        ("3 kurs","3 kurs"),
        ("4 kurs","4 kurs"),
    ]
    name=models.CharField(max_length=30,blank=True)
    bituruvchi=models.BooleanField("bituruvchu",default=False)
    ol_kitob=models.SmallIntegerField("olgan kitoblari soni",default=0)
    kursi=models.CharField(max_length=50,choices=k)
    def __str__(self) -> str:
        return f'{self.name} {self.kursi}'

class Record(models.Model):
    talab_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    kitob_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    olinan_sana=models.DateTimeField(auto_now_add=True)
    qaytarilgan_sana=models.DateTimeField(auto_now_add=True,)
    qaytardi=models.BooleanField("qaytaridi",default=True)
    def __str__(self) -> str:
        return f'{self.olinan_sana}'
class Admin(models.Model):
    name=models.CharField(max_length=50,blank=True)
    ishin_bosh=models.CharField(max_length=15)
    ishin_tush=models.CharField(max_length=15)
    def __str__(self) -> str:
        return f'{self.name}'