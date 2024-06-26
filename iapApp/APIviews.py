from rest_framework import viewsets
from rest_framework.response import Response
from .models import Jogo, IAP
from .serializers import JogoSerializer, IAPSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
import json

import django_filters

class IAPFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')
    valor_us = django_filters.NumberFilter(field_name='valor_us')

    class Meta:
        model = IAP
        fields = ['nome', 'valor_us']

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })


class JogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = {jogo.nome: self.request.build_absolute_uri(f'/iaps/{jogo.nome}') for jogo in queryset}
        return Response(data)

class IAPListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IAPSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = IAPFilter
    ordering_fields = ['valor_us']

    def get_queryset(self):
        jogo_nome = self.kwargs['jogo_nome']
        return IAP.objects.filter(jogo__nome=jogo_nome)

    @action(detail=False, methods=['post'])
    def setPrice(self, request, jogo_nome=None):
        iap_id = request.data.get('id')
        country = request.data.get('country')
        new_price = request.data.get('new_price')

        if not iap_id or not country or not new_price:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            iap = IAP.objects.get(nome=iap_id, jogo__nome=jogo_nome)
        except IAP.DoesNotExist:
            return Response({'error': 'IAP not found'}, status=status.HTTP_404_NOT_FOUND)

        price_dict = json.loads(iap.price)
        if country in price_dict['en-US']['iapPrices']:
            price_dict['en-US']['iapPrices'][country] = new_price
        else:
            price_dict['en-US']['iapPrices'][country] = new_price
        
        iap.price = json.dumps(price_dict)
        iap.save()
        iap.trata_precos()
        print(iap.iapPrices)
        return Response({'message': 'Price updated successfully'}, status=status.HTTP_200_OK)