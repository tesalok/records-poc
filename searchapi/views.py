from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from searchapi.models import Records
from django.db.models import Q

from searchapi.serailizers import RecordSerializer



# Create your views here.

class RecordListView(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Records.objects.all()
    pagination_class = LimitOffsetPagination
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = Records.objects.all()
            if request.GET.get('search'):
                keyword = request.GET['search']
                if len(keyword) >2:
                    if(keyword.find(",")>1):
                        queryset = queryset.filter(Q(name__icontains=keyword.split(',')[0]) & Q(state__icontains=keyword.split(',')[1]))
                    else:
                        queryset = queryset.filter(Q(name__icontains=keyword))
                else:
                    queryset = queryset.filter(Q(state__icontains=keyword))
            page = self.paginate_queryset(queryset)
            serializer = RecordSerializer(page,many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            print(e)
        
    def create(self, request, *args, **kwargs):
        for x in request.data:
            Records.objects.create(fips=x['fips'],state=x['state'],name=x['name'])
        return Response("data uploaded", status=status.HTTP_201_CREATED)