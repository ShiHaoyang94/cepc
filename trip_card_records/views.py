import os.path

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import requests, re
from django.contrib import messages

# Create your views here.
from cepc import settings
from .models import TripCardRecords



def post(request):
    if request.method == 'GET':

        return render(request, 'posts.html')


    elif request.method == 'POST':

        import base64

        import requests

        from datetime import datetime

        print(datetime.now())

        try:

            file_name = request.FILES['file_name']

            file_names = os.path.join(settings.MEDIA_ROOT, request.session.get('username'))

            with open(file_names, 'wb') as f:

                data = file_name.file.read()

                f.write(data)

            # 获取access_token

            # client_id 为官网获取的AK， client_secret 为官网获取的SK

            appid = '26149347'

            client_id = 'M9LCsi0v2Q9wHTDDiFQH8R06'

            client_secret = 'TasRoL1atapwOvwkdzNK9u67ctqM0NG7'

            print("appid:" + appid)

            print("client_id:" + client_id)

            print("client_secret:" + client_secret)

            token_url = "https://aip.baidubce.com/oauth/2.0/token"

            host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

            response = requests.get(host)

            access_token = response.json().get("access_token")

            # 调用通用文字识别高精度版接口

            request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

            # 以二进制方式打开图文件

            # 参数image：图像base64编码

            # 下面图片路径请自行切换为自己环境的绝对路径

            with open(file_names, "rb") as f:

                image = base64.b64encode(f.read())

            body = {

                "image": image,

                "language_type": "auto_detect",

                "detect_direction": "true",

                "paragraph": "true",

                "probability": "true",

            }

            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            request_url = f"{request_url}?access_token={access_token}"

            response = requests.post(request_url, headers=headers, data=body)

            content = response.json()

            print(content)
            word = str(content['words_result'])

            import re

            def find_chinese(file):

                chinese = re.findall(
                    '[*\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]', file)
                return ''.join(chinese)

            # ...
            result = str(word)
            result = find_chinese(result)
            print(result)
            ...
            re1 = r'到达或途经(.*?)结果包含'
            reResult = re.findall(re1, result)
            print(reResult)
            # 如果带*
            import datetime
            student_num = request.COOKIES.get('username')
            import datetime
            import re
            updated_time = datetime.datetime.now()
            handle = str(student_num) + str(
                ((re.findall(r"\d*", str(updated_time)))[0]) + ((re.findall(r"\d*", str(updated_time)))[2]) + (
                    (re.findall(r"\d*", str(updated_time)))[4]))
            if '*' in reResult[0]:

                try:
                    tcrecd = TripCardRecords.objects.get(handle=handle)
                    tcrecd.student_num = student_num
                    tcrecd.ifnormal = '1'
                    tcrecd.r_location = reResult[0]
                    tcrecd.creation_time = updated_time
                    tcrecd.save()
                    os.remove(file_names)
                    return HttpResponseRedirect('/successful')

                except Exception as e:

                    TripCardRecords.objects.create(student_num=student_num,
                                                   ifnormal='1',
                                                   r_location=reResult[0],
                                                   creation_time=updated_time,
                                                   handle=handle
                                                   )
                    os.remove(file_names)
                    return HttpResponseRedirect('/successful')
            else:
                try:
                    tcrecd = TripCardRecords.objects.get(handle=handle)
                    tcrecd.student_num = student_num
                    tcrecd.ifnormal = '0'
                    tcrecd.r_location = reResult[0]
                    tcrecd.creation_time = updated_time
                    tcrecd.save()
                    os.remove(file_names)
                    return HttpResponseRedirect('/successful')

                except Exception as e:

                    TripCardRecords.objects.create(student_num=student_num,
                                                   ifnormal='0',
                                                   r_location=reResult[0],
                                                   creation_time=updated_time,
                                                   handle=handle
                                                   )
                    os.remove(file_names)
                    return HttpResponseRedirect('/successful')

        except Exception as e:

            messages.success(request,
                             "图片不为空，现阶段我们支持的图片格式为：PNG、JPG、JPEG、BMP，请进行转码或更换图片，现阶段我们支持的图片大小为：base64编码后小于4M，分辨率不高于4096*4096，请重新上传图片，现阶段不支持 10M 或以上的数据包")

            return HttpResponseRedirect('/trip_card_records/post/')



