from django.shortcuts import render
from form_2.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, "form_2/index.html")

def user(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error invalid form")
    return render(request, 'form_2/user.html', {'form':form})
