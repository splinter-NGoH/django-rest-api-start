from django.urls import path, include
from rest_framework.routers import DefaultRouter    
from . import views

router = DefaultRouter()
# router.register('Helloviewsset', views.Helloviewsset, base_name='Helloviewsset')
router.register('UsesrProfileviewset', views.UsesrProfileviewset)
router.register('feed', views.UserProfileFeed)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='HelloApiView'),
    path('login/', views.UserLoginApiView.as_view(), name='UserLoginApiView'),
    path('', include(router.urls)), 
]
