from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext
from tweets.forms import SearchForm
from models import Bookmark

def search_page(request):
    form = SearchForm(request.GET)
    bookmarks = []
    show_results = False

    if form.is_valid():
        query = form.cleaned_data['query']
        keywords = query.split()
        q = Q()

        # preparing filter query
        for keyword in keywords:
            q = q & Q(title__icontains=keyword)

        # fetch bookmarks from db
        bookmarks = Bookmark.objects.filter(q)[:10]

    variables = RequestContext(request, {
        'form': form,
        'bookmarks': bookmarks,
        'show_results': show_results,
        'show_tags': True,
        'show_user': True
    })

    if request.GET.has_key('AJAX'):
        return render_to_response('bookmarks_list.html', variables)
    else:
        return render_to_response('search.html')

