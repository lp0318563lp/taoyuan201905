from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from carbon.models import carbon
from carbon.models import submitCarbonForm
from member.models import member



def Carbon(request):
    submitForm = submitCarbonForm()
    search_goods = request.GET.get('search_goods')
    memb = member.objects.get(memberId=request.session['user_id'])
    if search_goods != '' and search_goods is not None:
        qs = carbon.objects.all()
        qs = qs.filter(carbonName__icontains=search_goods)

    return render(request, 'carbon.html', locals()) 



def submitCarbon(request):
    mem = member.objects.get(memberId=request.session['user_id'])
    if request.method == 'POST':
        if 'id' in request.POST:
            for k in range(len(request.POST.getlist('corId'))):
                qu = float((carbon.objects.get(carbonId=request.POST.getlist('corId')[k]).carbonFootprint).split('kg')[0])
                total = round(qu*float(request.POST.getlist('id')[k]),2)
                print(total)#總共多少碳
                mem.dailyConsum = mem.dailyConsum+total
                mem.save()

        return HttpResponseRedirect('/carbon/')

