from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('clothes/', include('clothes.urls')),
    path('shoes/', include('clothes.urls')),
    path('accessories', include('clothes.urls')),
    path('NEW', include('clothes.urls')),
    path('about', include('main.urls')),
    path('search', include('main.urls')),
    path('paymant', include('main.urls')),
    path('favorites', include('main.urls')),
    path('purchase', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
