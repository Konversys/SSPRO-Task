import json

import jsonify as jsonify
from django.http import HttpResponse
from django.shortcuts import render
from .queries import *

# Парсинг всех направлений поездов с указанием
# Номера, Направления, и кодов станций отправления и прибытия
# С поиском по номеру и направлению

def direction(request):
    try:
        if 'type' in request.GET:
            directions = Execute(request.GET['data'], request.GET['type'], True)
        else:
            directions = Execute(None, 'all', True)
        count = len(list(Execute(None, 'all', True)))
        found = len(list(directions))
    finally:
        pass
    return render(request, 'direction.html', locals())


def direction_update(request):
    try:
        if 'type' in request.GET:
            directions = Execute(request.GET['data'], request.GET['type'], True)
        else:
            directions = Execute(None, 'all', True)
        count = len(list(Execute(None, 'all', True)))
        found = len(list(directions))
        json_data = ParseSqlToJSON(directions)
    finally:
        pass
    return HttpResponse(json.dumps(json_data), content_type="application/json")