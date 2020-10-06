from django.shortcuts import render
from django.http import Http404
import django_filters.rest_framework
from rest_framework import generics, viewsets, status
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.views import APIView
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
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kqargs):
        return self.create(request, *args, **kwargs)

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


