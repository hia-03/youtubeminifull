from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        image = request.FILES.get('image')
        agreed_terms = request.POST.get('agreed_terms')== 'on'
    #     User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password,image=image,agreed_terms=agreed_terms)
    #     return redirect('home')
    # return render(request,'cr_user.html')
        if password != confirm:
            return render(request, 'register.html',{'context': 'passwords are not same'})
        try:
            User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password,image=image,agreed_terms=agreed_terms)
            return redirect('home')
        except:
            return render(request,'register.html', {'context': 'this username or email already taken'})
    return render(request,'register.html')





def home(request):

    return render(request,'home.html')
    

def homelogins(request):
    
        if  request.session['id']:
            print('Hello world')
            return render(request,'homelogins.html',{'context': 'Welcome to admin panel'})
    
        return redirect('home')


# def login(request):
#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = User.objects.get(username=username,password=password)

#         if user:
#             request.session['id']=user.id
#             return redirect('home')
#         return render(request,'login.html',{'context': 'wrong username or password'})
#     return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            print('Hello world')
            request.session['id'] = user.id
            return redirect('loginhome')
        except:
            return render(request, 'login.html', {'context': 'Wrong username or password'})
    return render(request, 'login.html')




# def create_post(request):
#     try:
#         if request.session['id']:
                    
#             if request.method=='POST':
#                 title = request.POST.get('title')
#                 description = request.POST.get('description')
#                 user_id = request.session['id']
#                 video = request.FILES.get('video')
#                 Post.objects.create(title=title,description=description,user=User.objects.get(id=user_id),video=video)
#                 return redirect('home')
#         return render(request,'addpost.html')
#     except:
#         return redirect ('login')
    

def create_post(request):
    user_id = request.session.get('id')
    if not user_id:
        return redirect('login')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video = request.FILES.get('video')
        Post.objects.create(title=title,description=description,user_id=user,video=video)
        return redirect('home')

    return render(request, 'addpost.html')


def user_get_by_id(request, id):
    users = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user_id=users)
    return render(request, 'myvideo.html', {'users': users, 'posts': posts})



def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.description = request.POST.get("description")

        
        if request.FILES.get("video"):
            post.video = request.FILES.get("video")

        post.save()
        return redirect("video_detail", id=post.id)

    return render(request, "update_post.html", {"post": post})
