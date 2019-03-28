from django.core import serializers

from .models import *

def GetDirections():
    return Direction.objects.raw("SELECT * from direction")

def GetDirectionByValue(value):
    args = list()
    args.append('%' + value + '%')
    return Direction.objects.raw("SELECT * from direction where value LIKE %s", args)

def GetDirectionByNamePart(values):
    query = "SELECT * from direction where "
    values = values.split(' ')
    args = list()
    for i, item in enumerate(values):
        query += "name LIKE %s"
        args.append('%' + item + '%')
        if i < len(values) - 1:
            query += " AND "
    return Direction.objects.raw(query, args)

def ParseSqlToJSON(data):
    return serializers.serialize('json', data, fields=('id', 'value', 'name', 'fromx', 'tox', 'uid', 'date'))

def Execute(data, type, isSql):
    if (type == 'all'):
        if (isSql):
            return GetDirections()
        else:
            return ParseSqlToJSON(GetDirections())
    if (type == 'num'):
        if (isSql):
            return GetDirectionByValue(data)
        else:
            return ParseSqlToJSON(GetDirectionByValue(data))
    if (type == 'dir'):
        if (isSql):
            return GetDirectionByNamePart(data)
        else:
            return ParseSqlToJSON(GetDirectionByNamePart(data))
