from .views import MemberViewSet, MemberList, MemberBulkListCreateUpdateView
from django.conf.urls import re_path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('members', MemberViewSet)

urlpatterns = [
  re_path('^', include(router.urls)),
  re_path('^member/$', MemberList.as_view()),
  re_path("^upload/$", MemberBulkListCreateUpdateView.as_view()),
]
