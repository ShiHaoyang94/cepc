import json
import re

import requests
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import AbnormalRecords
# Create your views here.
def post(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    elif request.method == 'POST':
        LOCATION_P = request.POST['province']
        LOCATION_C= request.POST['city']
        TEMPERATURE = request.POST['TEMPERATURE']
        ABNORMAL_TYPE = request.POST['ABNORMAL_TYPE']
        ABNORMAL_DESC = request.POST['ABNORMAL_DESC']
        BTS_RECORD = request.POST['BTS_RECORD']
        pr_id = request.POST['ip']
        try:

            get_url = 'https://api.ipdatacloud.com/v1/query?ip='+pr_id+'&key=cdd89ad6bb2311ed94dd00163e25360e'
            headers = {
                'all_user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
            }
            response = requests.get(get_url, headers=headers)

            json = response.json()

            ip_province = json['data']['province']
            ip_city = json['data']['city']
            if not (LOCATION_P == ip_province and ip_city == LOCATION_C):
                messages.error(request, "ip地址与填报不符，请按实际填写")
                return HttpResponseRedirect('/trip_card_records/post')


            else:

                import datetime
                student_num = request.COOKIES.get('username')
                import datetime
                import re
                updated_time = datetime.datetime.now()
                handle=str(student_num)+str(
                        ((re.findall(r"\d*", str(updated_time)))[0]) + ((re.findall(r"\d*", str(updated_time)))[2]) + (
                        (re.findall(r"\d*", str(updated_time)))[4]))
                try:
                    abnormal = AbnormalRecords.objects.get(handle=handle)
                    abnormal.student_num=student_num
                    abnormal.location_c=LOCATION_C
                    abnormal.location_p=LOCATION_P
                    abnormal.temperature=TEMPERATURE
                    abnormal.creation_time=updated_time
                    abnormal.abnormal_type=ABNORMAL_TYPE
                    abnormal.abnormal_desc=ABNORMAL_DESC
                    abnormal.bts_record=BTS_RECORD
                    abnormal.save()
                    return HttpResponseRedirect('/trip_card_records/post')

                except Exception as e:


                    AbnormalRecords.objects.create(student_num=student_num,
                                                   location_c=LOCATION_C,
                                                   location_p=LOCATION_P,
                                                   temperature=TEMPERATURE,
                                                   creation_time=updated_time,
                                                   abnormal_type=ABNORMAL_TYPE,
                                                   abnormal_desc=ABNORMAL_DESC,
                                                   bts_record=BTS_RECORD,
                                                   handle=handle
                    )


                    return HttpResponseRedirect('/trip_card_records/post')


        except Exception as e:
            return HttpResponseRedirect('/busy')




