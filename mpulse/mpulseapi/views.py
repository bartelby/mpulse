from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics, viewsets
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(GenericViewSet,
                    CreateModelMixin, 
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_fields = ['id', 
                     'phone_number',
                     'client_member_id',
                     'account_id']
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


