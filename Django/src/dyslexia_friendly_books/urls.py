"""dyslexia_friendly_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from pages.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('Home/', home_view, name="home"),
    path('', Book_view, name = "book"),
    path('<int:book_num>/', editor_view, name="editor"),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('getTextSyllables/<str:txt>', getTextSyllables, name='getTextSyllables'),
    path('getSynoynms/<str:s>', getSynoynms, name='getSynoynms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
