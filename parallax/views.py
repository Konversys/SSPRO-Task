from django.shortcuts import render
from .queries import *

def direction(request):
    try:
        if 'type' in request.POST:
            if request.POST['type'] == 'all':
                directions = GetDirections();
            if request.POST['type'] == 'num':
                directions = GetDirectionByValue(request.POST['data'])
            if request.POST['type'] == 'dir':
                directions = GetDirectionByNamePart(request.POST['data'])
        else:
            directions = GetDirections()
        count = len(list(GetDirections()))
        found = len(list(directions))
    finally:
        pass
    return render(request, 'direction.html', locals())