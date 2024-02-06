"""
URL configuration for SyncSaga project.

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
from django.urls import path, include
from landing_page.views import *
from registration.views import *
from logining.views import *
from dashboard.views import *
from stories.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing_page"),
    path('register/', registration, name="registration"),
    path('login/', logining, name="logining"),
    path("logout/", logout_page, name="logout"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('create-story/', create_story, name="create_story"),
    path('view-story/', view_stories, name="view_story"),
    path('view-story/<int:story_id>/', view_story_detail, name='view_story_detail'),
    path('update-story-branch/<int:story_id>/', update_story_branch, name='update_story_branch'),
    path('view-story-changes/<int:story_id>/', view_story_changes, name='view_story_changes'),



]