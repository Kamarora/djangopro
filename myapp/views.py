from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from myapp.models import *
from .filters import UserFilter
import csv
from django.http import HttpResponse

def index(request):
    return render(request, "myapp/index.html", 
    {'title': 'All Price'})

def search(request):
    user_list = UserProfile.objects.all()
    print(request.GET)
    user_filter = UserFilter(request.GET, queryset=user_list)
    if 'btnval' in request.GET:
	    # Create the HttpResponse object with the appropriate CSV header.
	    response = HttpResponse(content_type='text/csv')
	    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	    writer = csv.writer(response)
	    writer.writerow(["Name", "Mobile", "Email", "Work Experience", "Skills"])
	    for data in user_filter.qs:
		    writer.writerow([data.name, data.mobile, data.email, data.work_exp, data.skills])

	    return response
    else:    
    	return render(request, 'myapp/user_list.html', {'filter': user_filter})



class UserListView(generic.ListView):
    model = UserProfile

