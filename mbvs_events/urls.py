"""mbvs_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from users.urls import users_router
from events.urls import events_router
from profiles.urls import profiles_router
from roles.urls import roles_router
from subscriptions.urls import subscriptions_router
from authentication.urls import registration_router
from auditorium.urls import auditoriums_router, videos_router

from authentication.views import RegistrationAPI, ChangePasswordView
from knox import views as knox_views
from authentication.views import LoginAPI
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users_router.urls)),
    path('api/', include(events_router.urls)),
    path('api/', include(profiles_router.urls)),
    path('api/', include(roles_router.urls)),
    path('api/', include(subscriptions_router.urls)),
    path('api/', include(auditoriums_router.urls)),
    path('api/', include(videos_router.urls)),
    # path('api-auth/', include(registration_router.urls)),
    path('api-auth/registration/', RegistrationAPI.as_view(), name='registration'),
    path('api-auth/login/', LoginAPI.as_view(), name='login'),
    path('api-auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api-auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api-auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api-auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
