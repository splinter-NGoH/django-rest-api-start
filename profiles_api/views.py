from re import search
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from . import models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class HelloApiView (APIView):

    serializer_class = serializers.HelloSerializer

    def get (self, requset, format=None):
        an_apiview = ['an_apiview test'] 

        return Response({'message': 'Hello', 'an_apiview':an_apiview})
    
    def post (self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put (self, request, pk=None):
        return Response({'method':'PUT'})
    
    def patch (self, request, pk=None):
        return Response({'method':'PATCH'})
    
    def delete (self, request, pk=None):
        return Response({'method':'DELETE'})

# class Helloviewsset (viewsets.model):
#     """test api """
#     serializer_class = serializers.HelloSerializer
#     def list (self, request):
#         a_viewset = [
#             'dummy data '
#         ]
#         return Response({'message':'Hello', 'a_view':a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response ({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve (self, request, pk=None):
        """getting an object by its id"""
        return Response({'http_method':'GET'})
    
    def update (self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update (self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy (self, request, pk=None):
        return Response({'http_method':'DELETE'})

class UsesrProfileviewset (viewsets.ModelViewSet):
    """creating and updating p[rofiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView (ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeed (viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItem
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    def perform_create (self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)