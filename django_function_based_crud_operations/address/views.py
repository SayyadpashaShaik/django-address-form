from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from address.forms import AddressForm
from address.models import Address

# Create your views here.


#  function deals with create list and retrieve list
def createandretrieve(request):
    form = AddressForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            nam = form.cleaned_data['name']
            mob = form.cleaned_data['mobile']
            pc = form.cleaned_data['pincode']
            st = form.cleaned_data['state']
            ad = form.cleaned_data['address']
            loc = form.cleaned_data['locality']
            cty = form.cleaned_data['city']
            toa = form.cleaned_data['type_of_address']
            md = Address(name=nam,mobile=mob,pincode=pc,state=st,address=ad,locality=loc,city=cty,type_of_address=toa)
            md.save()
            form = AddressForm()
        else:
            form = AddressForm()
    details = Address.objects.all()
    return render(request,'address/createandretrieve.html',{'details':details,'form':form})

# This is Update function
def update(request,pk):
    details = Address.objects.get(pk=pk)
    form = AddressForm(instance=details)
    if request.method == 'POST':
        form = AddressForm(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
            details = Address.objects.get(pk=pk)
            form = AddressForm(instance=details)
    details = Address.objects.all()      
    return render(request, 'address/update.html',{'form':form,'details':details})

#This is remove or delete function
def remove(request,pk):
    details = Address.objects.get(pk=pk)
    if request.method == 'POST':
        details.delete() 
        return HttpResponseRedirect('/')
    return render(request, 'address/createandretrieve.html')



