import json
from django.core import serializers
from django.http.response import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from amp_app.models import Customers


@csrf_exempt
def get_customer_by_area(request):
    if request.POST:
        customers = Customers.objects.filter(areas__id=request.POST['id'], is_customer=True)
        return HttpResponse(serializers.serialize('json', customers))

@csrf_exempt
def get_customer_by_number(request):
    if request.POST:
        customer = Customers.objects.get(account_number=request.POST['account_number'], is_customer=True)
        ret = {}
        if customer:
            ret= {
                "area_id":customer.areas.id,
                "customer_id": customer.id
            }

        return HttpResponse(json.dumps(ret, ensure_ascii=False))

def home(request):
    context = {}
    template = "index.html"
    return render_to_response(template, context, context_instance=RequestContext(request))