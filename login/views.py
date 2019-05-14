from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from login.models import RegisterForm
from login.models import UserForm
from member.models import member



# Create your views here.
def login(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect('/map/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "請檢查填寫的內容!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = member.objects.get(memberEmail=username)
                if user.memberPassword == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.memberId
                    request.session['user_name'] = user.memberEmail
                    return HttpResponseRedirect('/map/')
                else:
                    message = "密碼不正確"
            except:
                message = "用戶不存在!"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect("/map/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "請檢察填寫的內容!"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            name = register_form.cleaned_data['name']
            if password1 != password2:
                message = "兩次輸入的密碼不同!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = member.objects.filter(memberEmail=username)
                if same_name_user:
                    message = "用戶已經存在!"
                    return render(request, 'register.html', locals())
            new_user = member.objects.create()
            new_user.memberEmail = username
            new_user.memberPassword = password1
            new_user.memberName = name
            new_user.dailyConsum = None
            new_user.save()
            return HttpResponseRedirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return HttpResponseRedirect('/map/')
    request.session.flush()
    return HttpResponseRedirect('/map/')