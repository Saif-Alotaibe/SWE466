from django.shortcuts import render
from django.contrib import messages
from djmoney.money import Money
from .models import Resource
from decimal import Decimal


def view_resource(request):
	return render(request,
	              template_name="viewResources.html",
	              context={"resources": Resource.objects.all()}
	              )


def create_resource(request):
	if request.method == "POST":
		name = request.POST.get("name")
		resource_type = request.POST.get("resource_type")
		material_label = request.POST.get("material")
		max_number_of_resources = request.POST.get("max_number_of_resources")
		standard_rate = Money(decimal_places=2, currency="USD")
		overtime_rate = Money(decimal_places=2, currency="USD")
		cost_of_use = Money(decimal_places=2, currency="USD")
		standard_rate.amount = Decimal(request.POST.get("standard_rate"))
		overtime_rate.amount = Decimal(request.POST.get("overtime_rate", 0))
		cost_of_use.amount = Decimal(request.POST.get("cost_of_use", 0))
		Resource.objects.create(name=name,
		                        resource_type=resource_type,
		                        material_label=material_label,
		                        max_number_of_resources=max_number_of_resources,
		                        standard_rate=standard_rate,
		                        overtime_rate=overtime_rate,
		                        cost_of_use=cost_of_use,
		                        )
		messages.success(request, "Resource created successfully !")
	return render(request, template_name="createResources.html")
