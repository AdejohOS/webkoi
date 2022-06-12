
from django.http import Http404
from django.shortcuts import render

from django.db.models import Q
from . models import Message
from .utils import searchMessages, paginateMessages

# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


def sermons(request):
    messages, search_query = searchMessages(request)

    custom_range, messages = paginateMessages(request, messages, 3)

    context = {'messages': messages, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'pages/message.html', context)


def sermon_details(request, slug=None):
    # messageobj = Message.objects.get(id=pk)
    message_obj = None
    if slug is not None:
        try:
            message_obj = Message.objects.get(slug=slug)
        except Message.DoesNotExist:
            raise Http404
        except Message.MultipleObjectsReturned:
            message_obj = Message.objects.filter(slug=slug).first()

    context = {'message_obj': message_obj}
    return render(request, 'pages/message_detail.html', context)


def testimonies(request):
    context = {}
    return render(request, 'pages/testimonies.html', context)


def blog(request):
    context = {}
    return render(request, 'pages/blog.html', context)


def begin(request):
    context = {}
    return render(request, 'pages/begin.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)


def give(request):
    context = {}
    return render(request, 'pages/give.html', context)


def radio(request):
    context = {}
    return render(request, 'pages/radio.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)
