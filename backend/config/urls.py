from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/cameras/', permanent=False)),
    path('admin/', admin.site.urls),
    path('cameras/', include('camera.urls')),
]
