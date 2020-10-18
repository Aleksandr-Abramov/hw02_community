from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post, Group


def index(request):
    # latest = Post.objects.order_by("-pub_date")[:11]
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
