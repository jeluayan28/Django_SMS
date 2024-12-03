from django.shortcuts import render
from .forms import MessageForm
# Create your views here.

def landing_page(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print(f"Form data: {form.cleaned_data}")
            form.save()
            return render(request, 'landing_page.html', {'form': form, 'success': True})
        else:
            print("Form is invalid.")
    else:
        form = MessageForm()
    return render(request, 'landing_page.html', {'form': form})