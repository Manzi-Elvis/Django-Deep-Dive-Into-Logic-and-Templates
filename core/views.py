from django.shortcuts import render

def home(request):
    context = {
        "name": "Elvis",
        "messages": [
            "Django Templates are powerful",
            "Logic makes apps dynamic",
            "Forms make apps interactive"
        ],
        "age": 20
    }

    return render(request, "home.html", context)