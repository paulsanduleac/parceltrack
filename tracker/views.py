from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
from .models import Parcel


def index(request):
    parcel_list = Parcel.objects.order_by('-date_sent')[:5]
    # output = ', '.join([parcel.label for parcel in parcel_list])
    template = loader.get_template('tracker/index.html')
    context = {
        'parcel_list': parcel_list,
    }
    return render(request, 'tracker/index.html', context)


def parcel_detail(request, parcel_id):
    # try:
    #     parcel = Parcel.objects.get(pk=parcel_id)
    # except Parcel.DoesNotExist:
    #     raise Http404("This parcel does not exist.")
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    return render(request, 'tracker/parcel.html', {'parcel': parcel})
    # return render(request, 'tracker/parcel.html', {'parcel': parcel})
    # return HttpResponse("You're looking at parcel %s." % parcel_id)
