"""
URL configuration for studdy_buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from study_time.views import * # Import views from the authentication app
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static
from study_time.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home, name='home'),
    path('index/', index, name="recipes"),	 # index page
	path('login/', login_page, name='login_page'), # Login page
	path('register/', register_page, name='register'), # Registration page
	path('', include('study_time.urls')),
	path('start_study/', start_study, name='start_study'),
]


# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
