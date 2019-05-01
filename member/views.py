from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def member(request):
    return render(request, 'member.html')