import json
from django.test import TestCase, Client
from .models import Device

class DeviceTestCase(TestCase):
    # def setUp(self):
        # Device.objects.create(id='/devices/id1', deviceModel='/models/id1', name='Sensor', note='Testing a sensor.', serial='A0400102')
        # Device(id='/devices/id1', deviceModel='/models/id1', name='Sensor', note='Testing a sensor.', serial='A0400102')

    def test_create_device(self):
        client = Client()
        # response = client.post('/devices/', {
        #     'id': '/devices/id2',
        #     'deviceModel': '/models/id2',
        #     'name': 'Sensor 2',
        #     'note': 'Testing a sensor 2.',
        #     'serial': 'A0400103'
        #     })
        #send post as json
        response = client.post('/devices/', json.dumps({
            'id': '/devices/id2',
            'deviceModel': '/models/id2',
            'name': 'Sensor 2',
            'note': 'Testing a sensor 2.',
            'serial': 'A0400103'
            }), content_type='application/json')
        
        
        self.assertEqual(response.status_code, 201)
        # response = client.post('/devices/', {
        # 'id': '/devices/id3',
        # })
        response = client.post('/devices/', json.dumps({
            'id': '/devices/id3',
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Payload fields are missing.')
    def test_retrieve_device(self):
        client = Client()
        response = client.get('/devices/id2/')
        # print("["+str(response.content, encoding='utf8')+"]")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {   
                 'id': '/devices/id2',
                 'deviceModel': '/models/id2',
                 'name': 'Sensor 2',
                 'note': 'Testing a sensor 2.',
                 'serial': 'A0400103'
            }
        )

        response = client.get('/devices/id100/')
        self.assertEqual(response.status_code, 404)


