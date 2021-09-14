from django.http import HttpRequest, HttpResponse
import json
from task4.models import Numbers

def view(request: HttpRequest, obj=None) -> HttpResponse:
    name = ''
    try:
        obj.Numbers.objects.get(name = name)
        n = obj.n
    except:
        n = -1
    return HttpResponse(str(n))



def task4(request: HttpRequest):
    name = "MyNumbers"
    body = request.body.decode('utf-8')


    obj: Tuple[Numbers, bool] = Numbers.objects.get_or_create(name=name)
    cell, _created = obj

    if body == 'stop':

        counter = cell.n
        cell.n = 0
        cell.save()
        return HttpResponse(f"STOP! Sum is {counter!r}")

    elif body != 'stop':
        if body.isdigit() != True:

            return HttpResponse(f"Непонятно. Последняя сумма {cell.n!r}")
        else:
            cell.n += int(body)
            cell.save()

            return HttpResponse(f" Ваше число: {body!r}, Сумма: {cell.n!r}")



