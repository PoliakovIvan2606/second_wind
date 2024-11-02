from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
from user.models import User
from .models import Organization
def index(request):
    users = User.objects.prefetch_related('ogrn').all()
    ogrn = []
    for user in users:
        for org in user.ogrn.all():
            ogrn.append((user, org))
    return render(request, 'organization/index.html', context={'ogrn':ogrn})

def index2(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("<h2>Вам не доступна страница</h2>")

    return render(request, 'organization/index2.html')


def get_ogrn(request):
    ogrn = Organization.objects.values_list('ogrn', flat=True)
    return JsonResponse({'ogrn': list(ogrn)}, status=201)
