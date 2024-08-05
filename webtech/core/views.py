from django.shortcuts import render , redirect
from .forms import MyForm
# Create your views here.


def forms(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()

    return render(request, 'forms.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')