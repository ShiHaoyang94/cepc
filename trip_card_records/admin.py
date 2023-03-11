from django.contrib import admin

# Register your models here.
from trip_card_records.models import TripCardRecords
#
#
class TripCardRecordsManager(admin.ModelAdmin):
    list_display = ['student_num','ifnormal','r_location','creation_time']
    list_display_links = ['student_num']
    readonly_fields = ['student_num']
    list_filter = ['ifnormal','creation_time']
    search_fields = ['student_num','ifnormal','r_location','creation_time']
admin.site.register(TripCardRecords, TripCardRecordsManager)
from django.contrib import admin

admin.site.site_header = '疫情防控管理后台'  # 设置header
admin.site.site_title = '疫情防控管理后台'   # 设置title
admin.site.index_title = '疫情防控管理后台'
