import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Device
from django.views.decorators.csrf import csrf_exempt



# from .DynaDB import table
@csrf_exempt
def create_device(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            
            # content = body.get('id', None)
            # print(content)
            
            # data = request.POST
            
            id = data.get('id', None)
            deviceModel = data.get('deviceModel', None)
            name = data.get('name', None)
            note = data.get('note', None)
            serial = data.get('serial', None)
            if not id or not deviceModel or not name or not note or not serial:
                return HttpResponse(status=400, content='Payload fields are missing.')
            try:
                device = Device(id=id, deviceModel=deviceModel, name=name, note=note, serial=serial)
                # print(device.id)
                device.create_device()
                return HttpResponse(status=201,
                                    content='Device created.'
                                    )
            except Exception as e:
                print(e)
                return HttpResponse(status=500, content=str(e))
        except Exception as e:
            print(e)
            return HttpResponse(status=500, content="Internal server error.")

    else:
        return HttpResponse(status=405, content='Method not allowed.')

def retrieve_device(request, device_id):
    # print("retrieve_device",device_id)

    # data = device_data.get_queryset()
    try:
        device_data = Device.retrieve_device(device_id)
        if device_data is None:
            return HttpResponse(status=404, content='Device not found.')
        data = {
        'id': device_data.id,
        'deviceModel': device_data.deviceModel,
        'name': device_data.name,
        'note': device_data.note,
        'serial': device_data.serial
        }
        return JsonResponse(data, safe=True)
    except Exception as e:
        print(e)
        return HttpResponse(status=500, content="Internal server error.")

    #return a sample response
