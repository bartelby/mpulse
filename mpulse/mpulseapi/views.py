from django.shortcuts import render
from django.http import Http404
import django_filters.rest_framework
from rest_framework import generics, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Member
from .serializers import MemberSerializer, BulkMemberSerializer
from django.views.decorators.http import require_http_methods

#from rest_framework.urls import url

def validate_ids(data, field="id", unique=True):
    if isinstance(data, list):
        id_list = [int(x[field]) for x in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))
        return id_list
    return [data]

class MemberViewSet(GenericViewSet,
                    CreateModelMixin, 
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberList(generics.ListAPIView,):
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

## This class is not currently used.
class MemberBulkListCreateUpdateView(generics.ListCreateAPIView):

    serializer_class = BulkMemberSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data",{}), list):
            kwargs["many"] = True
        return super(MemberBulkListCreateUpdateView, self).get_serializer(*args, **kwargs)

    def get_queryset(self, ids=None):
        if ids:
            return Member.objects.filter(id__in=ids)
        return Member.objects.all()

    def post(self, request, *args, **kwargs):

        return super(MemberBulkListCreateUpdateView, self).post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        ids = validate_ids(request.data)

        instances = self.get_queryset(ids=ids)

        serializer = self.get_serializer(instances, data=request.data, partial=False, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data

        return Response(data)

    def get(self, request, *args, **kwargs):
        return Response({})

    def perform_update(self, serializer):
        serializer(save)
            
