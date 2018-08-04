from django.shortcuts import render

# Create your views here.

def index(request):
    # The variable "key" is now availabe for use in the template.
    return render(request, "viewer/index.html", context={"key": "value"})
    #                              ^ template file
