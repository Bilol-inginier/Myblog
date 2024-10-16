from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .form import *
from Mysite import settings


class PostlistView(ListView):
    queryset = Post.published.all()
    context_objects_name = 'posts'
    paginate_by = 3
    template_name = 'blog/index.html'



def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, status=Post.status.Active,
                             slug=post, publish__year=year, publish__month=month,publish__day=day)
    return  render(request, 'blog/post_detail.html', {'post': post})


def post_share(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.ACTIVE)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']}, вам пришло новое сообщение!"
            message = f"Посетите ``{post.title}`` по ссылке {post_url}"
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[cd['to']],
                fail_silently=False
            )
            return redirect('index')
    else:
        form = EmailPostForm
    context = {
        'title': 'Share with link',
        'form': form
    }
    return render(request, 'post_share.html', context)

