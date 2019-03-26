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