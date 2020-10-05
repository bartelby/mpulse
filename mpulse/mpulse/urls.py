"""mpulse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mpulseapi.models import Member
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 
                  'last_name',
                  'phone_number',
                  'client_member_id',
                  'account_id']
    
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)


admin.autodiscover()

urlpatterns = [
    path('', include(router.urls)),    
    path('admin/', admin.site.urls),
    path('api/v0.1/', include('rest_framework.urls', namespace='rest_framework'))
]
