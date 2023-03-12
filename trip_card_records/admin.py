from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.db.models import Q

from trip_card_records.models import TripCardRecords
#
class TripCardRecordsManager(admin.ModelAdmin):
    list_display = ['student_num','college_name','ifnormal','r_location','is_sign','info','creation_time']
    list_display_links = ['student_num']
    readonly_fields = ['student_num']
    list_filter = ['ifnormal','creation_time','college_name']
    search_fields = ['student_num','ifnormal','r_location','creation_time']
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(ifnormal="1")
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # 如果是超级用户，则返回所有资产信息。
            return qs
        else:  # 否则对 queryset 进行筛选并去重，仅返回请求用户可查看的资产信息。
            return qs.filter(is_sign='0',college_name=Group.objects.get(user=request.user))
admin.site.register(TripCardRecords, TripCardRecordsManager)
from django.contrib import admin
admin.site.site_header = '疫情防控管理后台'  # 设置header
admin.site.site_title = '疫情防控管理后台'   # 设置title
admin.site.index_title = '疫情防控管理后台'
