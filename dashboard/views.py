from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MessageForm

def landing_page(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('landing_page') 
        else:
            messages.error(request, 'Failed to send the message. Please try again.')
    else:
        form = MessageForm()

    return render(request, 'landing_page.html', {'form': form})
