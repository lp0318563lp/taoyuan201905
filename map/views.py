from django.shortcuts import render


# Create your views here.
from map.models import tripPlanForm
from map.models import mapAttractions


def map(request):
    attractions_info = mapAttractions.objects.all()
    select_form = tripPlanForm()
    return render(request, 'map.html', locals())




