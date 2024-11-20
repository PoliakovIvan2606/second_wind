from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from user.models import User
from .models import Organization
from user.forms import AddOgrnForm
import json

def index(request, ogrn):
    users = User.objects.prefetch_related('ogrn').all()
    ogrns = []
    for user in users:
        for org in user.ogrn.all():
            ogrns.append((user, org))
    return render(request, 'organization/index.html', context={'ogrns':ogrns, 'ogrn': ogrn})

def index2(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("<h2>Вам не доступна страница</h2>")

    return render(request, 'organization/index2.html')



@csrf_protect
def get_ogrn(request):
    user = request.user
    if request.method == "GET":
        ogrns = User.objects.get(email=user.email).ogrn.all().values_list('ogrn')
        return JsonResponse({'ogrn': list(ogrns)}, status=201)
    elif request.method == "POST":
        ogrn = json.loads(request.body)['ogrn']
        obj_ogrn, created = Organization.objects.get_or_create(ogrn=ogrn)
        user.ogrn.add(obj_ogrn)
        return JsonResponse({'status': 'ok'})
        