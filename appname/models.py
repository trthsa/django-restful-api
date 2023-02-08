from django.db import models
# from .DynaDB import dynamodbs
from .DynaDB import table

class Device():
    # id = models.CharField(max_length=100, primary_key=True)
    # deviceModel = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    # note = models.TextField()
    # serial = models.CharField(max_length=100)
    def __init__(
        self,
        id,
        deviceModel,
        name,
        note, 
        serial,
    ):
        self.id = id
        self.deviceModel= deviceModel
        self.name = name
        self.note = note
        self.serial = serial
    def create_device(self):
        # print("create_device",self.id)
        result = table.put_item(
            Item={
                'dv': str(self.id).split('/')[-1],
                'id': self.id,
                'deviceModel': self.deviceModel,
                'name': self.name,
                'note':  self.note,
                'serial': self.serial
            }
        )
        # print("result",result)
    def retrieve_device(device_id):
        response = table.get_item(
            Key={
                'dv': device_id
            }
        )
        if response.get('Item'):
            return Device(
         response.get('Item').get('id'),
         response.get('Item').get('deviceModel'),
         response.get('Item').get('name'),
         response.get('Item').get('note'),
         response.get('Item').get('serial'),
        )
        else:
            return None

        # return response.get('Item') if response.get('Item') else None
