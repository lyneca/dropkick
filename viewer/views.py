from django.http import Http404
from django.shortcuts import render

import sys
#raise Http404("sys.path = "+str(sys.path))
from get_data import accept_request

# Create your views here.

def index(request):
    # The variable "key" is now availabe for use in the template.
    return render(request, "viewer/index.html", context={"key": "value"})
    #                              ^ template file


def page(request, unit):
    try:
      page_context = {"project_name":"DropKick", "unit_name":str(unit).upper()}
    except:
      raise Http404("AHHHHHHH! I can't find your webpage! ... But you managed to end up here thought!")
    #try:
    accept_request(unit)
    #except:
    #  raise Http404("We are unable to get your unit's content due to it not being implemented. Also, django doesn't have Error 501 :.(")
    #page_context.update(unit_context)
    #print(page_context)

    return render(request, "viewer/unit_flow.html", page_context)

