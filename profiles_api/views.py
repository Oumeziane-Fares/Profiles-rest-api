from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a List of APIView Features"""
        an_apiview=[
            'Uses HTTP methodes as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most controle over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
