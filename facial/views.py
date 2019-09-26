import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.


class FacialView(View):
    def post(self, request):
        body = json.loads(request.body)
        count = body.get('count')
        if count == 1:
            data = {'state': 'success',
                    'message': 'Authentication success!', 'mode': 'img'}
        elif count == 2:
            data = {'state': 'error',
                    'message': 'Authentication fail!', 'mode': 'img'}
        else:
            data = {'state': 'error',
                    'message': 'Authentication fail! Please sign', 'mode': 'sign'}
        return JsonResponse(data)
