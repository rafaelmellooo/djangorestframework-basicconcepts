from rest_framework.viewsets import ModelViewSet
from ..models import Assessment
from .serializers import AssessmentSerializer


class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

