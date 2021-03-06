"""imagepicker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from api import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
# from django.views.static import serve

router = DefaultRouter()
router.register('', views.ImageViewSet, basename='image')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path(r'^image/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
