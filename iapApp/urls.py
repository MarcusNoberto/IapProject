from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, APIviews

from rest_framework.routers import DefaultRouter
from .APIviews import JogoViewSet, IAPListViewSet

router = DefaultRouter()
router.register(r'', JogoViewSet, basename='jogos')
router.register(r'iaps/(?P<jogo_nome>[\w\-]+)', IAPListViewSet, basename='iaps')


urlpatterns = [
    path('processar_iaps/', views.process_data_files, name='processar_iaps'),
]
urlpatterns += router.urls

