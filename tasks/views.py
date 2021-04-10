from django.shortcuts import render
from django.contrib import messages
from .models import Task


def view_tasks(request):
	
	return render(request,
	              template_name="viewTasks.html",
	              context={"tasks": Task.objects.all()}
	              )


def create_tasks(request):
	if request.method == "POST":
		task_name = request.POST.get("task_name")
		duration = request.POST.get("duration")
		start_date = request.POST.get("start_date")
		end_date = request.POST.get("end_date")
		Task.objects.create(name=task_name,
		                    duration=int(duration),
		                    start_date=start_date,
		                    end_date=end_date,
		                    )
		messages.success(request, "Task created successfully !")
	return render(request, template_name="createTasks.html")
