from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BondSerializer

from bonds.models import Bond



class BondViewSet(viewsets.ModelViewSet):
    # Defining view set:
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]




class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")




