from django.contrib import admin
from .models import *
# Register your models here.
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=("id","name","ol_kitob","kursi","bituruvchi")
#     list_display_links=("id","name")
#     list_editable=('kursi','ol_kitob','bituruvchi')
#     list_filter=('bituruvchi','kursi')
#     list_per_page=500
#     search_fields=('id','name','ol_kitob')

# @admin.register(Muallif)
# class MuallifAdmin(admin.ModelAdmin):
#     list_display=('id','muallif_n','hayot','kitoblar','jinsi','tugulan_sana','kitoblar_soni','yosh')
#     list_display_links=("id","muallif_n")
#     list_editable=("kitoblar_soni","hayot")
#     search_fields=('id','muallif_n','tugulan_sana')
#     list_filter=("hayot",)

# @admin.register(Admin)
# class Admin_Admin(admin.ModelAdmin):
#     list_display=('name','ishin_bosh','ishin_tush')
#     list_filter=('ishin_bosh',"ishin_tush")
#     search_fields=('name',)

# @admin.register(Record)
# class RecordAdmin(admin.ModelAdmin):
#     autocomplete_fields=('talaba_name','kitob_name')
#     list_display=('talab_name','kitob_name','olinan_sana','qaytarilgan_sana','qaytardi')
#     list_filter=('talab_name','kitob_name')
#     list_editable=("olinan_sana",'qaytarilgan_sana','qaytardi')


# admin.site.register(Book)
admin.site.register(Book)
admin.site.register(Admin)
admin.site.register(Record)
admin.site.register(Muallif)
admin.site.register(Student)
