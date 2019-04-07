from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponseNotFound
from django.shortcuts import redirect

from .utils import get_client_ip
from .models import Webmaster, Offer, Click


def redirector(request):

    offer_id = request.GET.get('offer_id', '')
    wm_id = request.GET.get('wmid', '')

    try:
        offer = Offer.objects.get(id=int(offer_id))
        wm = Webmaster.objects.get(id=int(wm_id))
    except:
        referer_url = request.META.get('HTTP_REFERER')
        if referer_url:
            return redirect(referer_url)
        else:
            return HttpResponseNotFound()


    click = Click.objects.create(offer=offer, webmaster=wm)

    click.client_user_agent = request.META['HTTP_USER_AGENT']

    client_ip = get_client_ip(request)
    click.client_ip = client_ip

    try:
        g = GeoIP2().city(client_ip)

        click.client_country = g['country_name']
        click.client_timezone = g['time_zone']
        click.client_city = g['city']
    except:
        pass

    click.save()

    return redirect(offer.url)
