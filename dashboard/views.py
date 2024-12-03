from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MessageForm

def landing_page(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # If form is valid, save the data and show success message
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('landing_page')  # Redirect to the same page to clear the form
        else:
            messages.error(request, 'Failed to send the message. Please try again.')
    else:
        # If it's a GET request, just render an empty form
        form = MessageForm()

    return render(request, 'landing_page.html', {'form': form})
