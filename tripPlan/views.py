from django.shortcuts import render

# Create your views here.
from tripPlan.models import tripPlanForm

def tripPlan(request):
    select_form = tripPlan(request.post)
    return render(request, 'map.html', {'select_form':select_form})