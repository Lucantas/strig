from rest_framework.serializers import ModelSerializer, IntegerField
from strig.web.models import User

class UserSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = User
        fields = ["id", "email", "name", "is_admin", "is_active", "creation_date"]
        