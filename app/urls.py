"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from backend.views.plate import PlateView
from backend.views.experiment import ExperimentView
from backend.views.experiment_indicator import ExperimentindicatorView
from backend.views.experiment_image import ExperimentimageView
from backend.views.project import ProjectView
from backend.views.user import UserView
from backend.views.user_project import UserProjectView





router = routers.DefaultRouter(trailing_slash=False)

# BELOW: example of url configuration for seperate components/modules

# note: router.register utilizes->  path('', include(router.urls))  <-seen in urlpatterns
router.register(r'plate', PlateView, 'plate')
router.register(r'experiment', ExperimentView, 'experiment')
router.register(r'experimentindicator', ExperimentindicatorView, 'experimentindicator')
router.register(r'experimentimage', ExperimentimageView, 'experimentimage')
router.register(r'project', ProjectView, 'project')
router.register(r'user', UserView, 'user')
router.register(r'userproject', UserProjectView, 'userproject')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    # path('', views.home, name="home")
]
