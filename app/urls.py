from django.urls import path
from .views import KlassAPIView, MehmonxonaAPIView, TravleAPIView

urlpatterns = [
    path('klass/', KlassAPIView.as_view(), name='klass-list'),
    path('klass/<int:pk>/', KlassAPIView.as_view(), name='klass-detail'),
    path('mehmonxona/', MehmonxonaAPIView.as_view(), name='mehmonxona-list'),
    path('mehmonxona/<int:pk>/', MehmonxonaAPIView.as_view(), name='mehmonxona-detail'),
    path('travle/', TravleAPIView.as_view(), name='travle-list'),
    path('travle/<int:pk>/', TravleAPIView.as_view(), name='travle-detail'),
]
