from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BondSerializer

from bonds.models import Bond



class BondViewSet(viewsets.ModelViewSet):
    # Defining, the user can only access the methods associated with this view if they are 
    # logged in and have an auth token:
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Create method allows a user to create a bond in the database using the Bond model:
    def create(self, request, *args, **kwargs):
        Bond.objects.create(
            user = request.user,
            isin = request.data['isin'],
            size = request.data['size'],
            currency = request.data['currency'],
            maturity = request.data['maturity'],
            lei = request.data['lei'],
        )

        # Returning the response of successfully saved Bond.
        return Response({'response': 'You have successfully saved your bond!'})




class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")




