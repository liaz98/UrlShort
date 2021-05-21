import random
import string
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.sites.shortcuts import get_current_site
from .models import UrlData
from rest_framework import status
from .serializers import UrlSerializer


# Create your views here.

class UrlView(APIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        url = request.data['url']
        slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
        current_site = get_current_site(request)
        new_url="http://{}/{}/".format(current_site, slug)
        new_url = UrlData(url=url, new_url=new_url)
        new_url.save()
        serializer = UrlSerializer(new_url)
        return Response(serializer.data)


def urlRedirect(request, slugs):
    current_site = get_current_site(request)
    new_url = "http://{}/{}/".format(current_site, slugs)
    data = UrlData.objects.get(new_url=new_url)
    return redirect(data.url)

