from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='workouts-home'),
    path('overview/', views.overview, name='workouts-overview'),
    path('search/', views.search, name='workouts-search'),
    path('<slug>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
