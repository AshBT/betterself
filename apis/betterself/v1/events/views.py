from apis.betterself.v1.events.serializers import SupplementEventCreateSerializer, SupplementEventReadOnlySerializer
from apis.betterself.v1.utils.views import BaseGenericListCreateAPIViewV1
from events.models import SupplementEvent


class SupplementEventView(BaseGenericListCreateAPIViewV1):
    model = SupplementEvent
    read_serializer_class = SupplementEventReadOnlySerializer
    write_serializer_class = SupplementEventCreateSerializer
    # add serializer_class!

    def get_serializer_class(self):
        request_method = self.request.method
        if request_method.lower() in ['list', 'get']:
            return self.read_serializer_class
        else:
            return self.write_serializer_class
