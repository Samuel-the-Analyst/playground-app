from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    # host = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = '__all__'

    # def get_host(self, obj):
    #     return obj.host.username
    
    