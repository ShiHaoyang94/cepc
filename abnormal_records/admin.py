from django.contrib import admin

# Register your models here.
from abnormal_records.models import AbnormalRecords
#
#
class AbnormalRecordsManager(admin.ModelAdmin):
    list_display = ['student_num','temperature','location_p','location_c','abnormal_type','abnormal_desc','bts_record','creation_time']
    list_display_links = ['student_num']
    readonly_fields = ['student_num']
admin.site.register(AbnormalRecords, AbnormalRecordsManager)
from django.contrib import admin

admin.site.site_header = '疫情防控管理后台'  # 设置header
admin.site.site_title = '疫情防控管理后台'   # 设置title
admin.site.index_title = '疫情防控管理后台'
