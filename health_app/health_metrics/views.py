from django.shortcuts import render, redirect  
from health_metrics.forms import PatientForm  
from health_metrics.models import Patient
# Create your views here.  
def pat(request):  
    if request.method == "POST":  
        form = PatientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/home')  
            except:  
                pass  
    else:  
        form = PatientForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    patients = Patient.objects.all()  
    return render(request,"show.html",{'patients':patients})  
def edit(request, id):  
    patient = Patient.objects.get(id=id)  
    return render(request,'edit.html', {'patient':patient})  
def update(request, id):  
    patient = Patient.objects.get(id=id)  
    form = PatientForm(request.POST, instance = patient)  
    if form.is_valid():  
        form.save()  
        return redirect("/home")  
    return render(request, 'edit.html', {'patient': patient})  
def destroy(request, id):  
    patient = Patient.objects.get(id=id)  
    patient.delete()  
    return redirect("/home")  