from django.shortcuts import render,HttpResponse,redirect
from medical.form import MedicinesForm
from medical.models import Medicines
import os
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')
@login_required
def addMedicines(request):
    obj = MedicinesForm()

    if request.method == "POST":
        obj = MedicinesForm(request.POST,request.FILES)

        if obj.is_valid():
            obj.save()

            return redirect('home')

        else:
            return HttpResponse("<h1>something is wrong</h1>")

    else:
        return render(request,'upload.html',{'form':obj})     
@login_required
def index(request):
    obj = Medicines.objects.all()
    return render (request,'list.html',{'form':obj})   

def update(request,medicnes_id):
    medicnes_id = int(medicnes_id)
    try:
        medicine_select = Medicines.objects.get(id=medicnes_id)

    except Medicines.DoesNotExists:
        #return HttpResponse("Something is wrong")
        return redirect('home')

    else:
        Medicines_form = MedicinesForm(request.POST or None ,instance = medicine_select)

        if Medicines_form.is_valid():
            old_img = ""
            if medicine_select.medicine_picture:
                old_img =  medicine_select.medicine_picture.path

                form = MedicinesForm(request.POST,request.FILES,instance= medicine_select)
                if form.is_valid():
                    if os.path.exists(old_img):
                        os.remove(old_img)  
                        form.save() 
            return redirect('home')
        return render(request,'update.html',{'form':Medicines_form})                


def delete(request,medicnes_id):
    medicnes_id = int(medicnes_id)
    try:
        medicine_select = Medicines.objects.get(id = medicnes_id)
        
    except Medicines.DoesNotExists:
        return redirect('home')
    
    medicine_select.delete()  
    return redirect('home')    


#def login(request):
    #return render(request,'registration/login.html')


@login_required
def logout(request):
    return render(request,"logout.html")        