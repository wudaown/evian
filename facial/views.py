import json
import base64
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from login.models import User
from course.models import Course, CourseIndex, CourseIndexType, Class, Attendance

# Create your views here.


class FacialView(View):
    def post(self, request):
        body = json.loads(request.body)
        count = body.get('count')
        image = body.get('image')
        image = image[23:]

        imgdata = base64.b64decode(image)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames

        # with open(filename, 'wb') as f:
        #     f.write(imgdata)

        # print(image)
        # print(type(image))

        if count == 1:
            data = {'state': 'success',
                    'message': 'Authentication success!', 'mode': 'img'}
            student = User.objects.get(matric_no = "U1620133D")
            course = Course.objects.get(course_code = "CZ3002")
            course_index = CourseIndex.objects.get(index = "12345")
            course_index_type = CourseIndexType.objects.get(course_index = course_index, class_type="lab")
            today = datetime.datetime.now()

            # today_date = today.date() + datetime.timedelta(days=1)
            today_date = today.date()
            
            time = course_index_type.time
            today_time = today.time()
            class_session = Class.objects.get(course_index_type = course_index_type, datetime__date = today_date)
            attendance = Attendance.objects.get(class_session = class_session, student = student)
            print(attendance)
            attendance.status = "present"
            attendance.attendance_time = today_time
            attendance.save()

        elif count == 2:
            data = {'state': 'error',
                    'message': 'Authentication fail!', 'mode': 'img'}
        else:
            data = {'state': 'error',
                    'message': 'Authentication fail! Please sign', 'mode': 'sign'}
        return JsonResponse(data)
