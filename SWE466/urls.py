"""SWE466 URL Configuration

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
from django.urls import path
from commons.views import home
from tasks.views import view_tasks, create_tasks
from resources.views import view_resource, create_resource
from commons.views import assign_resources_to_tasks, view_tasks_with_resources

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('tasks/', view_tasks, name="tasks"),
    path('createTasks/', create_tasks, name="createTasks"),

    path('resources/', view_resource, name="resources"),
    path('createResource/', create_resource, name="createResource"),
    
    path('assignResourcesToTasks/', assign_resources_to_tasks, name="assignTasksToResources"),
    path('tasksWithResources/', view_tasks_with_resources, name="viewTasksWithResources")
    
]
