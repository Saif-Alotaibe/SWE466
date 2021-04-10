from django.shortcuts import render
from django.contrib import messages
from tasks.models import Task
from resources.models import Resource
from django.db.models import Sum


def home(request):
    return render(request, template_name='base.html')


def assign_resources_to_tasks(request):
    if request.method == "POST":
        resources_ids = request.POST.getlist("resources")
        task = Task.objects.get(id=request.POST.get("task_id"))
        resources = Resource.objects.filter(id__in=resources_ids)
        for resource in resources:
            task.resources.add(resource)
        messages.success(request, "Resource(s) assigned successfully !")
    return render(request,
                  template_name="assignTasksToResources.html",
                  context={
                      "tasks": Task.objects.all(),
                      "resources": Resource.objects.all()
                  }
                  )


def view_tasks_with_resources(request):
    tasks = Task.objects.all()
    grand_total_cost = 0
    for task in tasks:
        sum_of_standard_rate = task.resources.aggregate(Sum("standard_rate"))
        task.total_resource_cost = sum_of_standard_rate['standard_rate__sum'] * 8 * task.duration
        grand_total_cost += task.total_resource_cost
    return render(request,
                  template_name="viewTasksWithResources.html",
                  context={"tasks": tasks, "grand_total": grand_total_cost}
                  )
