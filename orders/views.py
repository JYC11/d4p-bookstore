from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
from django.shortcuts import render
from django.contrib.auth.models import Permission
# Create your views here.

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    # to allow user to see books once payment is made
    # get the permission
    permission = Permission.objects.get(codename='special_status')
    # get the user
    u = request.user
    # add to user's permission set
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='jpy',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request,'orders/charge.html')
