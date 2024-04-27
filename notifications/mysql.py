from .models import Notification


class MysqlProcessor:
    def __init__(self):
        pass

    def process_notifications(self):
        notifications = Notification.objects.all().order_by('timestamp')
        notification_list = []
        for notification in notifications:
            notification_list.append(
                {
                    'id': notification.id,
                    'source_id':  notification.source_id,
                    'description': notification.description,
                    'timestamp': notification.timestamp,
                    'latitude': notification.latitude,
                    'longitude': notification.longitude,
                    'source_type': notification.source_type,
                    'dist_id': notification.dist_id
                }
            )
        return notification_list
