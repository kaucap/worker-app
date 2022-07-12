from rest_framework import serializers

from app_worker.models import Worker


class GeneralWorkerSerializer(serializers.ModelSerializer):
    """Сериализатор, для представления краткой информации о работниках"""

    class Meta:
        model = Worker
        fields = ['name', 'position']


class FullInfoWorkerSerializer(serializers.ModelSerializer):
    """Сериализатор, для представления полной информации о работниках"""

    class Meta:
        model = Worker
        fields = ['name', 'position', 'hired_at', 'salary', 'chief']
