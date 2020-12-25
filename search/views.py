from django.shortcuts import render, redirect
from django.urls import reverse
from .scraper import GoogleSearchPro
from .forms import SearchForm


def search(request, query, num):
    obj1 = GoogleSearchPro(query=query, number=num)
    result = obj1.search_url_title()
    title_qs = obj1.query

    # print(result)
    
    context = {
        # 'result': result.values(),
        'result': result.items(),
        'title_qs': title_qs,
    }
    return render(request, "search.html", context)


def index(request):
    form_class = SearchForm
    form = form_class(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            query = form.cleaned_data['query']
            num = form.cleaned_data['query_num']
            return redirect(reverse('search', kwargs={'query': query,
                                                        'num': num}))

    context = {
        'form': form,
    }
    return render(request, "index.html", context)