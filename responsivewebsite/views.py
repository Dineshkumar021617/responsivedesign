from django.shortcuts import render

# Create your views here.
def products(request):
    context = {}
    return render(request, 'responsivewebsite/twobreakpoints.html', context)  