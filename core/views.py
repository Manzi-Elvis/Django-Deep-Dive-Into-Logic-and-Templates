from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message
from .forms import MessageForm


def home(request):
    all_messages = Message.objects.all().order_by('-created_at')

    context = {
        "messages": all_messages
    }

    return render(request, "home.html", context)


def submit_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully!")
            return redirect("home")
    else:
        form = MessageForm()

    return render(request, "submit_message.html", {"form": form})