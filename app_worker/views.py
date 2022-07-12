from rest_framework import viewsets, permissions
from app_worker.models import Worker
from app_worker.serializers import GeneralWorkerSerializer, FullInfoWorkerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from app_worker.service import WorkerFilter
from rest_framework.filters import OrderingFilter


class GeneralWorkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для просмотра краткой информации обо всех работниках"""

    queryset = Worker.objects.all()
    serializer_class = GeneralWorkerSerializer


class FullInfoWorkerViewSet(viewsets.ModelViewSet):
    """Представление для просмотра подробной информации обо всех работниках, а также создания,
    обновления и удаления конкретного работника"""

    queryset = Worker.objects.all()
    serializer_class = FullInfoWorkerSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WorkerFilter
    ordering_fields = ('name', 'position', 'hired_at', 'salary', 'chief')

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'list': (permissions.IsAuthenticated,),
        'retrieve': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,)
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]