from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Records
import json
import sqlitecloud

def home(request):
    return render(request, 'index.html')

def check_id(request):
    print('received request, method:', request.method)
    if request.method == 'POST':

        print('request body:', request.body)
        
        data = json.loads(request.body)  # Parse the JSON body
        rut_ = data.get('rut')

        print('rut:', rut_)
        
        try:
            conn = sqlitecloud.connect("sqlitecloud://cyal6t7nhk.sqlite.cloud:8860/db.sqlite3?apikey=zCD1b2PUFALZ7j23hfjEXoYNWtABWxpsRlZjHlCb06E")
            # record = User.objects.get(rut=rut_)
            # print(f'query: SELECT * FROM app_user WHERE rut = "{rut_}"')
            cursor = conn.execute(f'SELECT * FROM app_user WHERE rut = "{rut_}"', (1,))
            record = cursor.fetchone()
            if record is None:
                return JsonResponse({"status": "invalid"}, status=400)
            # print('record:', record)
            # print('type:', type(record))
            # print('record member_type:', record[-2])
            # print('id:', record[0])
            # add new record to Records table
            # print(f'insert query: INSERT INTO app_records (USER_ID_id) VALUES ({record[0]})')
            conn.execute(f"INSERT INTO app_records (USER_ID_id, time_stamp) VALUES ({record[0]}, datetime('now'))")
            # Records.objects.create(USER_ID=record)
            # print('record member_type:', record[-2])
            return JsonResponse({"status": 'valid', 'member_type': record[-2], 'name': record[-4], 'last_name': record[-3] })
        except User.DoesNotExist:
            return JsonResponse({"status": "invalid"}, status=400)
        except:
            return JsonResponse({"status": 'unexpected error'}, status=500)

def check_id_local(request):
    print('received request, method:', request.method)
    if request.method == 'POST':

        print('request body:', request.body)
        
        data = json.loads(request.body)  # Parse the JSON body
        rut_ = data.get('rut')

        print('rut:', rut_)
        
        try:
            record = User.objects.get(rut=rut_)
            Records.objects.create(USER_ID=record)
            print('record:', record)
            print('record member_type:', record.member_type)
            return JsonResponse({"status": 'valid', 'member_type': record.member_type, 'name': record.name, 'last_name': record.last_name })
        except User.DoesNotExist:
            return JsonResponse({"status": "invalid"}, status=400)
        except:
            return JsonResponse({"status": 'unexpected error'}, status=500)