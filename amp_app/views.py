from django.core import serializers
from django.http.response import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from amp_app.models import Customers

@csrf_exempt
def get_customer_by_area(request):
    if request.POST:
        customers = Customers.objects.filter(areas__id=request.POST['id'],is_customer=True)
        return HttpResponse(serializers.serialize('json', customers))