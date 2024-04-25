from .models import Camera,Iot, Drone

class MysqlProcessor:
    def __init__(self):
        pass
    
    def get_all_devices(self):
        cameras = Camera.objects.all().order_by('district')
        device_info = {"all": {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], "10":[], "11":[], "12":[]}}
        for camera in cameras:
            data = {
                'id': camera.id,
                'index': camera.index,
                'latitude': camera.latitude,
                'longitude': camera.longitude,
                'address': camera.address,
                'dist_id': camera.district,
                'time': str(camera.time),
                'status': 'active' if camera.enabled else 'inactive',
                'type': 'camera'
            }
            device_info["all"][str(camera.district)].append(data)
            device_info["all"]["0"].append(data)
        
        iots = Iot.objects.all().order_by('district')
        for iot in iots:
            data = {
                'id': iot.station_id,
                'latitude': iot.latitude,
                'longitude': iot.longitude,
                'address': iot.address,
                'dist_id': iot.district,
                'status': 'active' if iot.enabled else 'inactive',
                'type': 'iot'
            }
            device_info["all"][str(iot.district)].append(data)
            device_info["all"]["0"].append(data)
            
        drones = Drone.objects.all().order_by('dist_id')
        for drone in drones:
            data = {
                'id': drone.id,
                'latitude': drone.latitude,
                'longitude': drone.longitude,
                'dist_id': drone.dist_id,
                'status': drone.status,
                'type': 'drone'
            }
            device_info["all"][str(drone.dist_id)].append(data)
            device_info["all"]["0"].append(data)
        return device_info