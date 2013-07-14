#; Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from .forms import UserInterestForm
from products.models import Item


def dashboard(request):
    temp_dict = {}
    interest_form = UserInterestForm()
    if request.method == "POST":
        interest_form = UserInterestForm(request.POST)
        if interest_form.is_valid():
            cleaned_data = interest_form.cleaned_data
            print "Email:", cleaned_data['email']
            print "Interest:", cleaned_data['interest']
            print "Brand:", cleaned_data['brand']
            print "Gender Type:", cleaned_data['gender_type']
            filtered_items = Item.objects.filter(category=cleaned_data['interest'],
                                                 brand=cleaned_data['brand'],
                                                 gender_type=cleaned_data['gender_type'])
            if cleaned_data['email']:
                interest_form.save()
            temp_dict['result'] = filtered_items
        else:
            temp_dict['result'] = "Form contains errors:" + str(interest_form.errors)
    temp_dict['interest_form'] = interest_form
    return render_to_response('dashboard/mainpage.html',
                              temp_dict,
                              context_instance=RequestContext(request))


def product_page(request,slug):
    temp_dict = {}
    return render_to_response('dashboard/product.html',
                              temp_dict,
                              context_instance=RequestContext(request))