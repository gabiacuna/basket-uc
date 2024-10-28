from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Records
import json

def home(request):
    return render(request, 'index.html')

def check_id(request):
    print('received request, method:', request.method)
    if request.method == 'POST':
        
        data = json.loads(request.body)  # Parse the JSON body
        rut_ = data.get('rut')
        
        try:
            record = User.objects.get(rut=rut_)
            Records.objects.create(USER_ID=record)
            return JsonResponse({"status": 'valid', 'member_type': record.member_type})
        except User.DoesNotExist:
            return JsonResponse({"status": "invalid"}, status=400)
        except:
            return JsonResponse({"status": 'unexpected error'}, status=500)