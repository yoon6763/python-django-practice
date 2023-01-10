from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)