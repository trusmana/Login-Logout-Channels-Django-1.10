from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from barang.forms import OrderForm,ProdukForm

def data_barang(request):
    product = Product.objects.all()
    return render(request,'data_barang.html',{'pro':product})

def edit_barang(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'edit_order.html')

@login_required
def new_order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order berhasil Dibuat.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data Tidak Ke Simpan', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form tidak valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new_order.html', {'form':form})

