import traceback

from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
import re
from django.core import mail

from cepc import settings

try:

    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if re.match("^/admin/", request.path):
            return None
        elif request.path == '/all_user/qunfa/':
            return None
        elif request.path == '/busy/':

            return None
        elif request.COOKIES.get('res_code'):
            if request.path != '/all_user/login/' and request.path != '/all_user/register/' and not re.match("^/all_user/check/",request.path) and not re.match(
                    "^/all_user/forget/", request.path):
                return HttpResponseRedirect('/all_user/login/')



        else:
            if request.session.get('username') or request.COOKIES.get('username'):
                if request.path != '/all_user/login/' and request.path != '/all_user/register/' and request.path != '/all_user/forget/':

                    if not re.match("^/abnormal_records/", request.path) and request.path != '/all_user/exit/' and not re.match(
                            "^/trip_card_records/", request.path):

                        return HttpResponseRedirect('/abnormal_records/post/')
                    elif re.match("^/trip_card_records/", request.path):
                        return None
                elif request.path == '/all_user/register/':
                    return None
                else:
                    return HttpResponseRedirect('/abnormal_records/post/')
            elif request.path == '/all_user/register/':
                return None
            elif request.path == '/all_user/forget/':
                return None
            elif request.path == '/all_user/login/':
                return None

            else:
                return HttpResponseRedirect('/all_user/login/')


# class IpMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         ip_address=request.META['REMOTE_ADDR']
#         print('我的地址'+ip_address)

# class ExceptionMW(MiddlewareMixin):
#     def process_exception(self, request, exception):
#         mail.send_mail(subject='校园防疫防控系统报错啦~', message=traceback.format_exc()+str(request.session.get('username'))+str(request.COOKIES.get('username')), from_email='352446506@qq.com',
#                        recipient_list=settings.EX_EMAIL)
#
#         return HttpResponseRedirect('/busy')