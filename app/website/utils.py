from django.db.models import Q
from . models import Message, Category, Minister
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# slugify
# import string, random
from django.utils.text import slugify


def searchMessages(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    categories = Category.objects.filter(category_name__icontains=search_query)
    ministers = Minister.objects.filter(minister_name__icontains=search_query)

    messages = Message.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(preacher__icontains=search_query) | Q(category__in=categories) | Q(minister__in=ministers)
    )
    return messages, search_query


def paginateMessages(request, messages, results):

    page = request.GET.get('page')
    paginator = Paginator(messages, results)

    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        messages = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        messages = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, messages
# slugify
