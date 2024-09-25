from django.shortcuts import render, redirect
from .models import Category, Product, Comment
# from .forms import LoginForm, CategoriForms
# from django.contrib.auth import authenticate, login, logout
from django.db.models import F, Count, Max 
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from django.urls import reverse 

from .forms import UserForm, LoginForm, Productform, CategoryForm, EditForm,ProductImagesForm
from django.contrib.auth import login as log, logout, authenticate


@login_required(login_url='login')
def edit(request,id):
	a = Product.objects.get(id=id)
	form = EditForm(instance=a)
	if request.POST:
		form = EditForm(request.POST,instance=a, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('myproduct')
	return render(request,'edit.html',{'form':form})
    

@login_required(login_url='login')
def delate(request, id):
    a = Product.objects.get(id=id)
    a.delete()
    return redirect('myproduct')



@login_required(login_url='login')
def myproduct(request):
    myproduct = Product.objects.filter(user=request.user)
    return render(request, 'myproduct.html', {'myproduct': myproduct})


    

# def edit(request,id):
#     a = Product.objects.get(id=id)
#     form  = ProductForm(instance=a)
#     if request.POST:
#         form = ProductForm(request.POST, instance=a, files=request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('home')
#     return render(request, 'single-post.html', {'form': form}) 



def create_category(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'name': 'create category'
    }
    return render(request, 'create.html', context)




@login_required(login_url='login')
def create_product(request):
    form = Productform()
    if request.POST:
        form = Productform(request.POST, files=request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('add_image', new_product.id)
    context = {
        'form': form,
        'name': 'create product'
    }
    return render(request, 'create.html', context)


def adding_image_product(request, id):
    offer = 'Rasm qoshishni hohlaysizmi?'
    
    form = ProductImagesForm()
    if request.POST:
        form = ProductImagesForm(files = request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.product = Product.objects.get(id=id)
            new_image.save()
            return redirect('add_image', id)
    return render(request, 'create.html', {'form': form, 'offer':offer, 'name': 'add image'})


def home(request):
    all_products = Product.objects.all()

    products = {
        
        'all_products': all_products 
    }
    return render(request, 'index.html', products)
    

# @login_required(login_url='login')
# def detail(request, id):
#     f = {'one': Product.objects.get(id=id)}
#     if request.POST:
#         name = request.POST['name']
#         Comment.objects.create(
#             comment=request.POST['izoh'],
#             product=f['one'],   
#         )
#         return redirect('detail')   
#     return render(request, "single-post.html", {'one': one})


 
# def detail(request, id):
#     f = {'one': Product.objects.get(id=id)}
#     if request.method == "POST":
#         name = request.POST.get('name')
#         Comment.objects.create(
#             comment = request.POST.get('izoh'),
#             product = f['one'],
#             user = request.user
#         )
#         return redirect(reverse('detail', args=[f.id]) + f"#{name}") 
#     elif request.POST.get('reply'):  
#         comment = Comment.objects.get(id=request.POST['comment_id'])
# 	    name = request.POST['name'] 
# 	    Comment.objects.create(
# 			comment = request.POST['reply'],

# 			product = f['one'],
# 			user = request.user,
# 			reply = comment
# 		)
# 		return redirect(reverse('detail', args=[f.id]) + f"#{name}" )
#     return render(request, "single-post.html", {'one': f['one']}) 




@login_required(login_url='login')
def detail(request, id):
    f = {'one': Product.objects.get(id=id)}
    if request.POST.get('izoh'):
        name = request.POST.get('name')
        Comment.objects.create(
            comment=request.POST.get('izoh'),
            product=f['one'],
            user=request.user
        )
        return redirect(reverse('detail', args=[f['one'].id]) + f"#{name}") 
    elif request.POST.get('reply'):  
        comment = Comment.objects.get(id=request.POST['comment_id'])
        name = request.POST['name'] 
        Comment.objects.create(
            comment=request.POST['reply'],
            product=f['one'],
            user=request.user,
            reply=comment
        )
        return redirect(reverse('detail', args=[f['one'].id]) + f"#{name}")
    return render(request, "single-post.html", {'one': f['one']})


 



# def detail(request, id):
# 	f = {'one': Product.objects.get(id=id)}
# 	if request.method == "POST":
# 		name = request.POST.get('name') 
# 		Comment.objects.create(
# 			comment = request.POST.get('izoh'),
# 			product = f['one'],
# 			user = request.user	
# 		)
# 		return redirect(reversed('detail', id=id))
	
# 	elif request.POST.get('reply'):
# 		comment = Comment.objects.get(id=request.POST['comment_id'])
# 		name = request.POST('name')
# 		Comment.objects.create(
# 			comment = request.POST['reply'],

# 			product = f,
# 			user = request.user,
# 			reply = comment
# 		)
# 		return redirect(reversed('detail', id=id))
# 	return render(request, 'single-post.html', {'one': f['one']})


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')    

def search(request):
    return render(request, 'search-result.html')  


def signup(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form, 'name': 'signup'})

def login(request):
    form =LoginForm()
    if request.POST:
        username = request.POST['username']
        parol = request.POST['password']
        user = authenticate(request, username=username, password=parol)
        if user is not None:
            log(request, user)
            messages.success(request, 'Siz login boldingiz!') 
            return redirect('home')
        messages.warning(request, 'Sizda nimadir xatolik bor...')
    return render(request, 'main.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('home')
 