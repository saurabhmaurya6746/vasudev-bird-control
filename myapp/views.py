from django.shortcuts import render,HttpResponse, redirect
# from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .models import Contact  
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import InquiryForm  # Import the new model
from django.contrib import messages  # For success messages

# def index(request):
#     return render(request, "index.html")  # Load index page

def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        comment = request.POST.get("comment")

        # Save data to InquiryForm table
        InquiryForm.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            number=number,
            comment=comment
        )
        # Send Email Notification
        send_mail(
            "New Inquiry Form Submission",
            f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nNumber: {number}\nComment: {comment}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )


        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect("index")  # Redirect back to index.html

    return render(request, "index.html")   # If no POST request, redirect to index


def about(request):
    return render(request,'about.html')
    
def blog(request):
    return render(request,'blog.html')
    
# def contact(request):
#     return render(request,'contact.html')
    
def gallery(request):
    return render(request,'gallery.html')
    
def birdnettingservices(request):
    return render(request,'bird-netting-services.html')

def birdspikesystem(request):
    return render(request,'bird-spike-system.html')

def sportnet(request):
    return render(request,'sport-net.html')

def carparkingnetsystem(request):
    return render(request,'car-parking-net-system.html')


def swimmingpool(request):
    return render(request,'swimming-pool-protect-net-system.html')

def safetynet(request):
    return render(request,'safety-nets.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")

        # Save data to database
        Contact.objects.create(name=name, email=email, phone=phone, comment=comment)
        # Send Email Notification
        send_mail(
            "New Contact Form Submission",
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nComment: {comment}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Add a success message
        messages.success(request, "Your message has been sent successfully!")

        return redirect("contact")  # Redirect back to contact page

    return render(request, "contact.html")  # Load contact form page


def exploring(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")

        # Save data to database
        Contact.objects.create(name=name, email=email, phone=phone, comment=comment)
        # Add a success message
        messages.success(request, "Your message has been sent successfully!")

        return redirect("exploring-the-essential")  # Redirect back to contact page

    return render(request,'exploring-the-essential.html')

def Keepingpigeons(request):
    return render(request,'Keeping-Pigeons.html')

def pleatedpigeon(request):
    return render(request,'pleated-pigeon.html')


def spikes(request):
    return render(request,'spikes.html')



def bird(request):
    return render(request,'bird.html')

