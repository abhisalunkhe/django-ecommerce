from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    fea_item = feature_items.objects.all()
    cate_tshirt1 = cate_tshirt.objects.all()
    cate_blazer1 = cate_blazer.objects.all()
    cate_sunglass1 = cate_sunglass.objects.all()
    cate_kids1 = cate_kids.objects.all()
    cate_poloshirt1 = cate_poloshirt.objects.all()
    return render(request,'index.html',{'fea_item': fea_item, 'cate_tshirt': cate_tshirt1, 'cate_blazer': cate_blazer1, 'cate_sunglass': cate_sunglass1, 'cate_kids': cate_kids1, 'cate_poloshirt': cate_poloshirt1})

def abc404(request):
    return render(request,'404.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contactus(request):
    return render(request,'contact-us.html')

def login(request):
    return render(request,'login.html')

def productdetails(request):
    return render(request,'product-details.html')

def shop(request):
    return render(request,'shop.html')

def wishlist(request):
    return render(request,'wishlist.html')

def nike(request):
    d = categ_nike.objects.all()
    return render(request,'nike.html',{'data': d})

def underarmour(request):
    d = categ_underarmour.objects.all()
    return render(request,'underarmour.html',{'data': d})

def adidas(request):
    d = categ_adidas.objects.all()
    return render(request,'adidas.html',{'data': d})

def puma(request):
    d = categ_puma.objects.all()
    return render(request,'puma.html',{'data': d})

def asics(request):
    d = categ_asics.objects.all()
    return render(request,'asics.html',{'data': d})

def fendim(request):
    d = categ_men_fendi.objects.all()
    return render(request,'fendim.html',{'data': d})

def fendiw(request):
    d = categ_women_fendi.objects.all()
    return render(request,'fendiw.html',{'data': d})

def guessm(request):
    d = categ_men_guess.objects.all()
    return render(request,'guessm.html',{'data': d})

def guessw(request):
    d = categ_women_guess.objects.all()
    return render(request,'guessw.html',{'data': d})

def valentinom(request):
    d = categ_men_valentino.objects.all()
    return render(request,'valentinom.html',{'data': d})

def valentinow(request):
    d = categ_women_valentino.objects.all()
    return render(request,'valentinow.html',{'data': d})

def diorm(request):
    d = categ_men_dior.objects.all()
    return render(request,'diorm.html',{'data': d})

def diorw(request):
    d = categ_women_dior.objects.all()
    return render(request,'diorw.html',{'data': d})

def versacem(request):
    d = categ_men_versace.objects.all()
    return render(request,'versacem.html',{'data': d})

def versacew(request):
    d = categ_women_versace.objects.all()
    return render(request,'versacew.html',{'data': d})

def armani(request):
    d = categ_men_armani.objects.all()
    return render(request,'armani.html',{'data': d})

def prada(request):
    d = categ_men_prada.objects.all()
    return render(request,'prada.html',{'data': d})

def dolceandgabbana(request):
    d = categ_men_dolceandgabbana.objects.all()
    return render(request,'dolceandgabbana.html',{'data': d})

def chanel(request):
    d = categ_men_chanel.objects.all()
    return render(request,'chanel.html',{'data': d})

def gucci(request):
    d = categ_men_gucci.objects.all()
    return render(request,'gucci.html',{'data': d})

def kids(request):
    d = categ_kids.objects.all()
    return render(request,'kids.html',{'data': d})

def fashion(request):
    d = categ_fashion.objects.all()
    return render(request,'fashion.html',{'data': d})

def households(request):
    d = categ_households.objects.all()
    return render(request,'households.html',{'data': d})

def interiors(request):
    d = categ_interiors.objects.all()
    return render(request,'interiors.html',{'data': d})

def clothing(request):
    d = categ_clothing.objects.all()
    return render(request,'clothing.html',{'data': d})

def bags(request):
    d = categ_bags.objects.all()
    return render(request,'bags.html',{'data': d})

def shoes(request):
    d = categ_shoes.objects.all()
    return render(request,'shoes.html',{'data': d})

def register(request):
    if request.method == "POST":
        if User.objects.filter(username = request.POST['uname']).exists():
            print("User Already Exists")
        elif User.objects.filter(email = request.POST['email']).exists():
            print("Email Already Existed")
        else:
            u = User.objects.create_user(first_name = request.POST['name'],username = request.POST['uname'],email = request.POST['email'],password = request.POST['psw'])
            u.save()
            return redirect('/login')
    else:
        return render(request,'login.html')
    
def loginForm(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['uname'],password = request.POST['psw'])
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('Invalid Credentials')
            return redirect('loginForm')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def get_in_touch(request):
    if request.method == "POST":
        data = getintouch.objects.create(name = request.POST['name'],email = request.POST['email'],subject = request.POST['subject'],message = request.POST['message'])
        data.save()
        return redirect('/shop')
    else:
        return render(request,'contact.html')