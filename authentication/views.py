from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from gfg import settings
from  django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token


#update profile
from django.contrib.auth.hashers import check_password
def change_username(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('home')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user
        if check_password(current_password, user.password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return redirect('home')
            else:
                # Handle case where new and confirm password do not match
                messages.error(request, 'New password and confirm password do not match')
                return redirect('change_password')
        else:
            # Handle case where current password is incorrect
            messages.error(request, 'Current password is incorrect')
            return redirect('change_password')


#single page for property
from django.shortcuts import render
from .models import Property

def single_property(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'single_property.html', {'property': property})


#propery
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from .models import Property
@login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'upload.html', {'form': form})


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

#my propertys
def my_properties(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'my_properties.html', {'properties': properties})

#delet my property 
from django.shortcuts import render, get_object_or_404, redirect
def delete_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    if property.user != request.user:
        raise PermissionError('You can only delete properties that you have uploaded.')
    property.delete()
    return redirect('my_properties')


#profile pic
from .models import Profile
def upload_profile_picture(request):
    if request.method == 'POST':
        profile_picture = request.FILES['profile_picture']
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None
        if profile:
            profile.profile_picture = profile_picture
            profile.save()
        else:
            Profile.objects.create(user=user, profile_picture=profile_picture)
        return redirect('home')


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
def adm(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def pro(request):
    return render(request,"properties.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to Property Mangement System"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Property Mangement System \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nPrashant Kumar Rai"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email "
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
        
        
    return render(request, "authentication/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('adm')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')




#contact seller
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Property

def contact(request):
    property = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')
        property_id = request.POST.get('property_id')
        seller_email = request.POST.get('seller_email')

        # send email
        subject = "New Request"
        email_body = f"Dear Sir,\n\nWe are delighted to inform you that a potential buyer is interested in your property on Property Pioneers. Below are the details of the interested buyer:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nMessage: {message}\n\nPlease feel free to contact them using the details provided above to further discuss the sale of your property.\n\nThank you for choosing Property Pioneers for all your property needs.\n\nBest regards,\nPrashant Kumar rai\nProperty Pioneers Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [seller_email]
        send_mail(subject, email_body, from_email, to_list, fail_silently=True)

    if 'property_id' in request.POST:
        property_id = request.POST['property_id']
        property = Property.objects.get(id=property_id)

    context = {
        'property': property,
    }
    return render(request, 'single_property.html', context)
