from django.http import HttpRequest, HttpResponse
import json
from typing import Optional
from task4.models import Numbers
from django.views.decorators.csrf import csrf_exempt

def view(request: HttpRequest, obj=None) -> HttpResponse:
    name = ''
    try:
        obj.Numbers.objects.get(name = name)
        n = obj.n
    except:
        n = -1
    return HttpResponse(str(n))


def get_user_name(request: HttpRequest) -> Optional[str]:
    username = request.headers.get("x-user") or None
    return username


@csrf_exempt
def task4(request: HttpRequest):
    if request.method != 'POST':
        return HttpResponse(status=405)
    else:
        username = get_user_name(request)
        if not username:
            return HttpResponse(status=403)
        name = "MyNumbers"
        obj: Tuple[Numbers, bool] = Numbers.objects.get_or_create(name=name)
        cell, _created = obj

        body = json.loads(request.body)
        if not body:
            return HttpResponse(status=422)
        else:
            if type(body) == str:
                if body == "stop"  or body == '"stop"' or body == "'stop'":
                    counter = cell.n
                    cell.n = 0
                    cell.save()
                    return HttpResponse(f"{counter}")
                if body.isdigit() or body == "0":
                    return HttpResponse(status=422)
            elif type(body) == int:
                if body <= -101 or body >= 101:
                    return HttpResponse(status=422)

                else:
                    cell.n += body
                    cell.save()
                    return HttpResponse(f"{cell.n!r}")



























