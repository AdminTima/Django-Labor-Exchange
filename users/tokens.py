from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(user, "it is user")
        print(user.email, "it is user email")
        token = super().get_token(user)
        token["email"] = user.email
        if getattr(user, "employer", None):
            token["role"] = "employer"
        else:
            token["role"] = "employee"
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
