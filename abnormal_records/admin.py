from django.contrib import admin

# Register your models here.
from abnormal_records.models import AbnormalRecords
#
#
from .resource import AbnormalRecordsResource

from import_export.admin import ImportExportModelAdmin
    # 导入刚刚写好的Resource

    # 重写一个管理类，并绑定到模型类
@admin.register(AbnormalRecords)
class AbnormalRecordsColumnsAdmin(ImportExportModelAdmin):
    resource_class = AbnormalRecordsResource
    list_display = ['student_num','temperature','location_p','location_c','abnormal_type','abnormal_desc','bts_record','creation_time']
    list_display_links = ['student_num']
    readonly_fields = ['student_num']
    hoices_gender = [

    ]

    class AgeListFilter(admin.SimpleListFilter):
        title = (u'是否返校')
        parameter_name = 'bts_record'

        def lookups(self, request, model_admin):
            return (
                (0, '暂缓返校'),
                (1, '今日返校'),
                (3, '已返校')
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(bts_record='0')
            if self.value() == '1':
                return queryset.filter(bts_record='1')
            if self.value() == '3':
                return queryset.filter(bts_record='3')



    list_filter = ['student_num','location_p','location_c','abnormal_type','abnormal_desc',AgeListFilter,'creation_time']
    search_fields = ['student_num','location_p','location_c','abnormal_type','abnormal_desc']

from django.contrib import admin

admin.site.site_header = '疫情防控管理后台'  # 设置header
admin.site.site_title = '疫情防控管理后台'   # 设置title
admin.site.index_title = '疫情防控管理后台'
