from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    text = 'Главная страница'
    context = {
        'text': text
    }
    return render(request, template, context)

# def group_posts(request, slug):
#     return HttpResponse(f'Группа: {slug}')

def group_post(request):
    template = 'posts/group_list.html'
    title = 'group-list'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template, context)


