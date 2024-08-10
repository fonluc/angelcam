from django.urls import path
from .views import CameraListView, CameraDetailView, login_redirect, home

urlpatterns = [
    path('', CameraListView.as_view(), name='camera-list'),  # Lista de câmeras
    path('112860/', CameraDetailView.as_view(), name='camera-detail'),  # Corrigido para corresponder ao caminho
    path('112859/', CameraDetailView.as_view(), name='camera-detail'),  # Corrigido para corresponder ao caminho
    path('login/', login_redirect, name='login-redirect'),
    path('home/', home, name='home'),                                                # Página inicial
]
