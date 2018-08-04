from django.http import Http404
from django.shortcuts import render

# Create your views here.

def index(request):
    # The variable "key" is now availabe for use in the template.
    return render(request, "viewer/index.html", context={"key": "value"})
    #                              ^ template file


def page(request, unit):
    try:
      page_context = {"project_name":"DropKick", "unit_name":str(unit)}
    except:
      raise Http404("AHHHHHHH! I can't find your webpage! ... But you managed to end up here thought!")
    return render(request, "viewer/view_units.html", page_context)

