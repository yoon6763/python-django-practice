from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


# Create your views here.
def signup(request):

    # POST 일 때는 입력한 데이터로 사용자 등록
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        # GET 일 때는 회원가입 폼을 보여줌
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
