from django.http import HttpResponse #displays what we want

def aboutUs(request):
    return HttpResponse("welcome to mypage")
