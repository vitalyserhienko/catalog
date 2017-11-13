from rest_framework import serializers
from sto.models import Sto, StoService

class StoSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, sto):
        request = self.context.get('request')
        logo_url = sto.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Sto
        fields = ('id', 'name' , 'phone', 'adress', 'logo')


class ServicesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, service):
        request = self.context.get('request')
        image_url = service.image.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = StoService
        fields = ('id', 'name' , 'service_type', 'description', 'image', 'price')
