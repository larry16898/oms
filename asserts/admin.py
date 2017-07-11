from django.contrib import admin
from .models import Assert,AssertChangeRecord,AssertChangeRelation,AssertCategory

# Register your models here.
@admin.register(AssertCategory)
class AssertCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Assert)
class AssertsAdmin(admin.ModelAdmin):
    list_display = ('assert_code','category','owner','location','assert_status','ip_address','comment')
    list_per_page = 50
    search_fields = ['assert_code','location']
#    list_editable = ['assert_code','category','owner','location','assert_status','ip_address','comment']

@admin.register(AssertChangeRecord)
class AssertChangeRecordAdmin(admin.ModelAdmin):
    list_display = ('name','change_content')

@admin.register(AssertChangeRelation)
class AssertChangeRelationAdmin(admin.ModelAdmin):
    list_display = ('assert_related','change_record_related','created','modified')
