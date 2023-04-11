from django.urls import path

from .views import *

urlpatterns = [
    path('',loginview,name='login'),
    path('bosh_sahifa/', bosh_sahifa, name='bosh_sahifa'),
    path('kitoblar/',kitoblar, name='kitob'),
    path('kitob_1/<int:son>/',kitob_1, name='kitob_1'),
    path('mualliflar/',mualliflar, name='mualliflar'),
    path('muallif/<int:son>',muallif, name='muallif'),
    path('talabalar/',talabalar, name='talabalar'),
    path('talaba/<int:son>/',talaba, name='talaba'),
    path('recordlar/',recordlar, name='recordlar'),
    path('record/<int:son>/',record, name='record'),
    path('talaba_ochir/<int:son>/',talaba_ochir, name='talaba_ochir'),
    path('kitob_ochir/<int:son>/',kitob_ochir, name='kitob_ochir'),
    path('muallif_ochir/<int:son>/',muallif_ochir, name='muallif_ochir'),
    path('record_ochir/<int:son>/',record_ochir, name='record_ochir'),
    path('adminlar/',adminlar, name='adminlar'),
    path('admin_edit/<int:son>/',Admin_edit, name='admin_edit'),
    ]