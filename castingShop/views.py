from django.shortcuts import render,redirect
from .models import Products
# Create your views here.
from django.views.generic import ListView,DetailView
from django.urls import reverse
from . import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
class Home(ListView):

    model = Products
    context_object_name = 'products'
    template_name = 'castingShop/products/list.html'



class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'castingShop/products/details.html'

    def get_context_data(self,**kwargs):
        self.object = self.get_object()
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        form = forms.ProductForm(self.request.POST or None)
        context["form"] = form
        return context

    def post(self,request,*args,**kwargs):

        context = self.get_context_data()
        if context["form"].is_valid():
            # human = True
            context["form"].save(commit=False)
            form = context["form"]
            employee =500
            electricity = 3000

            order = int(form['quantity'].value())+0.01
            raw_order = order*28000
            sand=15*(2*order)
            gobar = 20*(2*order)
            pattern_change=5000*order
            wastage = 0.044*order
            coal = 2700*order
            wood = 500*order
            renew = 0.15*order
            total_cost = raw_order+sand+gobar+pattern_change+coal+wood+electricity+employee

            # form.total_cost = total_cost
            # form.company_profit = (total_cost+1)-wastage+renew

            context["form"].save()
            messages.success(request, "ThankYou for CheckIN. Your total_cost is {}".format(total_cost))
            return redirect(reverse('castingShop:home'))
        return super(ProductDetailView, self).render_to_response(context)

def CustomizeView(request):
    if request.method == "POST":
        form = forms.CustomizeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            employee =500
            electricity = 3000
            order = int(form['quantity'].value())+0.01
            raw_order = order*28000
            sand=15*(2*order)
            gobar = 20*(2*order)
            pattern_change=5000*order
            wastage = 0.044*order
            coal = 2700*order
            wood = 500*order
            renew = 0.15*order
            total_cost = raw_order+sand+gobar+pattern_change+coal+wood+electricity+employee

            #saving non-provided fields

            # form["total_cost"] = total_cost
            # form['company_profit'] = (total_cost+1)-wastage+renew

            form.save()
            messages.success(request, "ThankYou for CheckIN. Your total cost will be {}".format(total_cost))
            return redirect(reverse('castingShop:home'))
    else:
        form = forms.CustomizeForm()

    return render(request,'castingShop/customizeform.html',{'form':form})
