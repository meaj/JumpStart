from django.template.loader import get_template
from django.utils import datetime_safe
from django.http import HttpResponse
from django.views.generic import View

class generatePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('workshops/invoice.html')
        context = {
            'today': 'nh',
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        html = template.render(context)
        return HttpResponse(html)