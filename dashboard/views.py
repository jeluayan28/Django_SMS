from django.shortcuts import render
from django.contrib import messages
from .forms import MessageForm

def landing_page(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            form = MessageForm() 
        else:
            messages.error(request, 'Failed to send the message. Please try again.')

    return render(request, 'landing_page.html', {'form': form})
