"""
URL configuration for hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Hackathon_API import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('add-hackathon/', views.hackathon_details.as_view()),
                  path('<int:pk>/update-hackathon/', views.hackathon_details.as_view()),
                  path('user-login/', views.login.as_view()),
                  path('user-register/', views.register.as_view()),
                  path ('hackathon-registrations/', views.hackathonRegistration.as_view()),
                  path ('view-registered-hackathons/<int:pk>/', views.hackathonRegistration.as_view()),
                  path ('deregister-hackathon/<int:user_id>/<int:hackathon_id>', views.hackathonRegistration.as_view()),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
