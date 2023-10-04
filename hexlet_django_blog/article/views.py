from django.shortcuts import render

articles = [
    {'title': 'Summer', 'author': 'Ivan'},
    {'title': 'Images', 'author': 'Anton'},
    {'title': 'How to Django', 'author': 'Andrey'},
    {'title': 'Planning', 'author': 'Evgeny'},
    {'title': 'Story telling', 'author': 'Valentin'},
    {'title': 'Photography', 'author': 'Valery'},
]
def index(request):
    return render(request, 'article/index.html', context={
        'pagetitle': 'Articles',
        'articles': articles,
    })
