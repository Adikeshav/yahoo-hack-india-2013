#; Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from .forms import UserInterestForm


def dashboard(request):
    temp_dict = {}
    interest_form = UserInterestForm()
    if request.method == "POST":
        interest_form = UserInterestForm(request.POST)
        if interest_form.is_valid():
            if not interest_form.cleaned_data['email']:
                temp_dict['result'] = "Show results only"
            else:
                temp_dict['result'] = "Show results and set alert to " + interest_form.cleaned_data['email']
        else:
            temp_dict['result'] = "Form contains errors:" + str(interest_form.errors)
    temp_dict['interest_form'] = interest_form
    return render_to_response('dashboard/mainpage.html',
                              temp_dict,
                              context_instance=RequestContext(request))
