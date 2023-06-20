from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile , Post ,Like ,Comment
from django.contrib.auth.hashers import make_password
from itertools import chain
# Create your views here.


@login_required(login_url='core:signup')
def home(request):
    posts = Post.objects.all()
    user_profile = Profile.objects.get(username = request.user)
    user = Profile.objects.all()
    context = {
        'userprofile': user_profile,
        'posts': posts,
        'user' :user,
        "crn_user": request.user.username
    }
    return render(request,'index.html',context)

def Sign_up(request):
    if request.method == 'POST' :
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
         
        if pass1 == pass2 and len(pass1) >= 8:
            if User.objects.filter(email = email).exists():
                messages.info(request , 'email taken')
                return redirect('core:signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'username taken')
                return redirect('core:signup')
            else:
                user = User.objects.create(email = email,username = username , password = make_password(pass1))
                user.save()
                user_object = User.objects.get(username = username)
                profile_user = Profile.objects.create(username = user_object)
                profile_user.save()
                auth.login(request,user)
                return redirect("core:setting")
        else:
            messages.info(request,'Passwords are not the same')
            return render(request,"signup.html")
    
    else:
        return render(request,"signup.html")
    

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("core:home")
        else:
            messages.info(request,"invalid user")
            return redirect('core:signin')
    else:
        return render(request,'signin.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'signin.html')



login_required(login_url="core:signup")
def setting(request):
    user_profile = Profile.objects.get(username = request.user)
    if request.method == "POST":
         
        name = request.POST['nickname']
        if User.objects.filter(username=name).exists():
                messages.info(request,"username taken")
                user_profile.save()
                return redirect("core:setting")
        if request.FILES.get('pic') == None:
            user_profile.address = request.POST["loc"]
            user_profile.bio = request.POST["bio"]
            user_profile.nickname = request.POST["nickname"]
            user_profile.save()
        elif request.FILES.get('pic') != None:
            user_profile.images = request.FILES.get("pic")
            user_profile.address = request.POST["loc"]
            user_profile.bio = request.POST["bio"]
            user_profile.nickname = request.POST["nickname"]
            user_profile.save()

    return render(request,'setting.html',{"proflie":user_profile})



def upload(request):
    if request.method == "POST":
        user = request.user.username
        caption = request.POST["caption"]
        image = request.FILES.get('image')
        new_post = Post.objects.create(user=user,caption=caption,image = image)
        new_post.save()
        messages.info(request,"Post save")
        return redirect("/")
    else:
        messages.info(request,"Post not save")
        return redirect('/')




login_required(login_url="core:signup")
def profile(request,username):
    user_object = User.objects.get(username = username)
    user_profile = Profile.objects.get(username=user_object)
    user_posts = Post.objects.filter(user=user_profile.username.username)
    context = {
        "user-object":user_object,
        "user_profile" : user_profile,
        "user_posts" : user_posts,
        "posts":len(user_posts)
    }
    return render(request,"profile.html",context)


def like(request,post_id):
    post = Post.objects.get(id = post_id)
    is_like = Like.objects.filter(post_id = post.id, user = request.user.username)
    
    if is_like.exists():
        is_like.delete()
        post.no_likes -= 1
        post.save()
        return redirect('/')
    elif not is_like.exists():
        new_like = Like.objects.create(post_id = post.id, user = request.user.username)
        new_like.save()
        post.no_likes += 1
        post.save()
        return redirect('/')
    

def comment(request):
    if request.method == "POST":
        author = request.user.username
        user = request.POST['user']
        comment = request.POST['comment']
        id = request.POST['postid']
        post = Post.objects.get(id= id)
        new_comment = Comment.objects.create(author=author,post=post,user=user,comment=comment,slug=comment[0:3])
        new_comment.save()
        return redirect('/')
    else:
        return redirect('/')
    

def delete(request,post_id):
    post = Post.objects.filter(id = post_id)
    post.delete()
    return redirect("/")



def dlcm(request,comment_slug):
    comment = Comment.objects.get(slug=comment_slug)
    comment.delete()
    return redirect("/")

def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(username=user_object)

    if request.method == 'POST':
        if 'searching' in request.POST:
            search = request.POST['searching']
        else:
            search = False
        username_object = User.objects.filter(username__icontains=search)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(user_id=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
        context = {
            'user_profile': user_profile, 
            'username_profile_list': username_profile_list
        }
    return render(request, 'search.html', context)
