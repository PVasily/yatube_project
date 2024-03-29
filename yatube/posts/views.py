from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, template, context)


def group_post(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    title = f'Вы в сообществе {group}'
    context = {
        'group': group,
        'title': title,
        'posts': posts
    }
    return render(request, template, context)
