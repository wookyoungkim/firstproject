from django.shortcuts import render, redirect
from blogweb.models import Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post(request):
    posts = Post.objects
    return render(request, 'post.html', {'posts': posts})
    
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.POST['title']  #GET->POST : GET은 PUT에서 밀어줬을때만, POST로 하면 key깂대로
    post.body = request.POST['body']

    post.pic = request.FILES['pic']

    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/' + str(post.id))

def delete(request, post_id):
    review = get_object_or_404(Post, id=post_id)
    review.delete()
    return redirect('/')