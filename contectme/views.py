from django.shortcuts import render,redirect
from.models import ContectHere
from django.contrib import messages

# Create your views here.
def contecthere(request):
    # con=ContectHere.objects.all()
    if request.method=='POST':
        full_name=request.POST['full_name'] 
        phone=request.POST['phone']  
        company_name=request.POST['company_name'] 
        email=request.POST['email'] 
        subject=request.POST['subject'] 
        message=request.POST['message'] 

        if ContectHere.objects.filter(phone=phone).exists():
                messages.warning(request,'phone no. already exist')
                return redirect('contact')
        else: 
                ContectHere.objects.filter(email=email).exists() 
                messages.warning(request,'email exist')
                return redirect('contact') 
    else:

                contectheres=ContectHere(full_name=full_name,phone=phone,company_name=company_name,email=email,subject=subject,message=message)
                contectheres.save()
                messages.success(request,'you have contect with us')
                return redirect ('contact')

    return render(request,'contact.html')    