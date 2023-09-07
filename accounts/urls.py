from django.urls import path
from .views import UserViewSet,Setviews 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'signup'}), name='signup'),
    path('verify_email/', UserViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
    path('verify_token/',Setviews.as_view(), name='verify_token'),
]