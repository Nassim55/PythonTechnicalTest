# External library imports:
import requests

# Rest framework imports:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Model imports:
from bonds.models import Bond

# Serializer imports:
from .serializers import BondSerializer


'''Viewset handles user interaction with the Bond model. Allows a user to create bonds and retreive
bonds that they are authourised to retreive'''
class BondViewSet(viewsets.ModelViewSet):
    # Defining, the user can only access the methods associated with this view if they are 
    # logged in and have an auth token:
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    # List method allows a user to get all of the bond they have saved in the database
    # Only allows the user to retreive bonds that they are authorised to get:
    def list(self, request):
        # Checking if there is a filter in the get request. If there isn't return the 
        # full list of bonds related to the user:
        legal_name = request.GET.get('legal_name')
        if legal_name:
            try:
                requested_bond = Bond.objects.filter(user = request.user).get(legal_name = legal_name)
                serializer = BondSerializer(requested_bond)
            except Bond.DoesNotExist:
                return Response(status = status.HTTP_404_NOT_FOUND)
        else:
            requested_bond = Bond.objects.filter(user = request.user)
            serializer = BondSerializer(requested_bond, many=True)

            # If the serializer contains no data return a 404 error:
            if len(serializer.data) == 0:
                return Response(status = status.HTTP_404_NOT_FOUND)

        return Response({ 'response': { 'messgage': 'You have successfully retreived your bond/bonds', 'data': serializer.data } })


    # Create method allows a user to create a bond in the database using the Bond model:
    def create(self, request, *args, **kwargs):
        # Before creating a bond we need to get the legal name from the external API:
        lei = request.data['lei']
        response = requests.get(f'https://leilookup.gleif.org/api/v2/leirecords?lei={lei}')
        data = response.json()

        # Defining the legal name and removing whitespace:
        legal_name = data[0]['Entity']['LegalName']['$']
        legal_name = legal_name.replace(' ', '')

        # Creates the bond object oin the database:
        Bond.objects.create(
            user = request.user,
            isin = request.data['isin'],
            size = request.data['size'],
            currency = request.data['currency'],
            maturity = request.data['maturity'],
            lei = request.data['lei'],
            legal_name = legal_name,
        )

        # Returning the response of successfully saved Bond.
        return Response({'response': 'You have successfully saved your bond!'})

    




class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")




