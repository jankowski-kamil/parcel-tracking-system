from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_rest_passwordreset.views import ResetPasswordConfirm
from dj_rest_auth.views import LoginView

from parcel_tracking.users.models import User

from .serializers import UserSerializer, PasswordResetConfirmSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CustomResetPasswordConfirmView(ResetPasswordConfirm):
    serializer_class = PasswordResetConfirmSerializer


class CustomLoginView(LoginView):

    def get_response(self):
        original_message = super().get_response()
        response = {"user": original_message.data["user"]}
        original_message.data = response
        return original_message
