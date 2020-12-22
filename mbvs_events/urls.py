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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users_router.urls)),
    path('api/', include(events_router.urls)),
    path('api/', include(profiles_router.urls)),
    path('api/', include(roles_router.urls)),
    path('api/', include(subscriptions_router.urls)),
]
