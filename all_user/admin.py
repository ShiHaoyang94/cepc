from django.contrib import admin

# Register your models here.
from all_user.models import AllUser
#
#
# class UserManager(admin.ModelAdmin):
#     list_display = ['student_num','name','id_num','campus','college_name','class_name','phone','user_type','email','password','privileges','is_active']
#     list_display_links = ['student_num']
#     readonly_fields = ['student_num']
# admin.site.register(AllUser, UserManager)
from django.contrib import admin

admin.site.site_header = '疫情防控管理后台'  # 设置header
admin.site.site_title = '疫情防控管理后台'   # 设置title
admin.site.index_title = '疫情防控管理后台'

from .models import AllUser
# 取一个插件内的管理器
from import_export.admin import ImportExportModelAdmin
# 导入刚刚写好的Resource
from .resource import AllUserResource
# 重写一个管理类，并绑定到模型类
@admin.register(AllUser)
class AllUserColumnsAdmin(ImportExportModelAdmin):
    # 对接资源类
    resource_class = AllUserResource
    # 类表页面展示哪些，与导入导出无关

    list_display = ['student_num','name','id_num','campus','college_name','class_name','phone','user_type','email','password','privileges','is_active']
    list_display_links = ['student_num']
    readonly_fields = ['student_num']