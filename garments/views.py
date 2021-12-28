from django import template
from django.shortcuts import render, redirect
from django.contrib import messages
from garments.models import Order, tailor, Completed
from garments.forms import OrderForm, tailors
from django.conf import settings
import datetime
from django.http import HttpResponse, response
from django.template.loader import get_template
import qrcode
import qrcode.image.svg
from io import BytesIO
from xhtml2pdf import pisa
extend=[] 
order=[]
def OrderDetails(request):
    global order
    order.sort(key= lambda x: x.order_received, reverse=True)
    d=datetime.date.today()
    if request.method=='POST':
        #print("hello")
        delids=request.POST.getlist('del[]')
        y=request.POST.get("inp")
        if delids:
            for i in delids:
            #print(i)
                x=Order.objects.get(Order_id=i)
                order.remove(x)
                comp=Completed(serial_number=x.serial_number, order_name=x.order_name, amount=x.amount, salesman_assigned=x.salesman_assigned, booking_date=x.order_received, mobile_number=x.mobile_number, tailor_assigned=x.tailor_assigned, advance=x.advance)
                comp.save()
                x.delete()
            return redirect('/')
        if y:
            li=[]
            for i in Order.objects.all():
                if i.serial_number.startswith(y) or i.mobile_number.startswith(y):
                    li.append(i)
            context={"active":li}
            return render(request, 'orders.html',context)
    context={"active":order, 'date': d}
    return render(request, 'orders.html',context)

def FullDaySales(request):
    global extend,order
    x=Order.objects.all().order_by('-order_received')
    days31=[1,3,5,7,8,10,12]
    date_today=int(datetime.date.today().strftime("%d"))
    month_this=int(datetime.date.today().strftime("%m")[1:])
    year_this=int(datetime.date.today().strftime("%y"))
    today=[]
    for i in x:
        if i.order_received==datetime.date.today():
            today.append(i)
            if i not in order: order.append(i)
            continue
        d=int(i.order_received.strftime("%d"))
        m=int(i.order_received.strftime("%m")[1:])
        y=int(i.order_received.strftime("%y"))
        y_leap=True if y%4==0 and y%100!=0 or y%400==0 else False
        if m==month_this:
           left=abs(d-date_today)
        elif m==2:
           if y_leap:
                left=29-d+date_today
           else:
                left=28-d+date_today
        elif m in days31:
           left=31-d+date_today
        else:
            left=30-d+date_today
        if left<=15:
            if i not in order: order.append(i)
        else:
            if i not in extend: extend.append(i)
    d=datetime.date.today()
    if request.method=='POST':
        y=request.POST.get("inp")
        x=request.POST.get('date')
        slipname=request.POST.get('slips')
        print(x,slipname)
        if y:
            li=[]
            for i in Order.objects.all():
                if i.serial_number.startswith(y) or i.mobile_number.startswith(y):
                    li.append(i)
            context={"today":li}
            return render(request, 'fullday.html',context)
        if x:
            if slipname=='tailor': 
                info=tailor.objects.all()
                tail={i.tailor_name:[] for i in info}
                for i in Order.objects.all():
                    if str(i.order_received)==x:
                        tail[i.tailor_assigned].append(i)
                final={}
                for i in tail:
                    if tail[i]:
                        final[i]=tail[i]
                template_path='tailorslip.html'
                context={'tailor':final , 'date':x }
                res=HttpResponse(content_type='application/pdf')
                name=str(x)+ '_tailorslip'+'.pdf'
                res['Content-Disposition']='attachment; filename={} '.format(name)
                temp=get_template(template_path)
                htm=temp.render(context)
                pisa_status=pisa.CreatePDF( htm, dest=res)
                return res
            elif slipname=='received': 
                now=[]
                for i in Order.objects.all():
                    if str(i.order_received)==x: now.append(i)
                template_path='ReceivedSlip.html'
                context={'today':now, 'date':x}
                res=HttpResponse(content_type='application/pdf')
                name=str(x)+ '_Receivedslip'+'.pdf'
                res['Content-Disposition']='attachment; filename={} '.format(name)
                temp=get_template(template_path)
                htm=temp.render(context)
                pisa_status=pisa.CreatePDF( htm, dest=res)
                return res
            elif slipname=='completed': 
                now=[]
                for i in Completed.objects.all():
                    if str(i.order_completed)==x: now.append(i)
                template_path='doneslip.html'
                context={'today':now,'date':x}
                res=HttpResponse(content_type='application/pdf')
                name=str(x)+ '_Completedslip'+'.pdf'
                res['Content-Disposition']='attachment; filename={} '.format(name)
                temp=get_template(template_path)
                htm=temp.render(context)
                pisa_status=pisa.CreatePDF( htm, dest=res)
                return res
            else:
                messages.warning(request,'Invalid Input')
                return redirect('/')
        elif slipname:
            messages.warning(request,'Invalid Input')
            return redirect('/')
    context={"today":today, 'date': d, 'flag':0}
    return render(request,'fullday.html',context)

def AddOrder(request):
    form_class= OrderForm
    if request.method=='POST':
        form=OrderForm(request.POST)
    
        if form.is_valid():
            
            order=form.save(commit=False)
            order.tailor_assigned=order.tailor_assigned.upper()
            order.save()

            messages.success(request,'Order Placed Successfully!')
            return redirect('/')
        return render(request, 'addorder.html' , {'form': form})
    return render(request, 'addorder.html', {'form': form_class})

def Addtailor(request):
    form_class= tailors
    if request.method=='POST':
        form=tailors(request.POST)
        if form.is_valid():

            tailor1=form.save(commit=False)
            tailor1.tailor_name=tailor1.tailor_name.upper()
            tailor1.save()
            messages.success(request,'New Tailor Added Successfully!')
            return redirect('/')
        return render(request, 'addtailor.html' , {'form': form})
    return render(request, 'addtailor.html', {'form': form_class})

def Pending(request):
    global extend
    if request.method=='POST':
        #print("hello")
        delids=request.POST.getlist('del[]')
        for i in delids:
            #print(i)
            x=Order.objects.get(Order_id=i)
            extend.remove(x)
            comp=Completed(serial_number=x.serial_number, order_name=x.order_name, amount=x.amount, salesman_assigned=x.salesman_assigned, booking_date=x. order_received, mobile_number=x.mobile_number, tailor_assigned=x.tailor_assigned, advance=x.advance)
            comp.save()
            x.delete()
        return redirect('/')
        
    return render(request, 'pending.html',{'pend': extend})

# run - pip install xhtml2pdf 
def GenerateBill(request,serial_no):
    info=Order.objects.get(Order_id=serial_no)
    # template_path='bill.html'
    context={ 'x': info,'date': datetime.date.today(), 'item': info.order_name.split(',')}
    # print(info.Order_id)
    # res=HttpResponse(content_type='application/pdf')
    # name=info.serial_number+'.pdf'
    # res['Content-Disposition']='attachment; filename={} '.format(name)
    # temp=get_template(template_path)
    # htm=temp.render(context)
    # pisa_status=pisa.CreatePDF( htm, dest=res)
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make("https://instagram.com/novelty_store_raymond?utm_medium=copy_link", image_factory=factory, box_size=4)
    stream = BytesIO()
    img.save(stream)
    context["svg"] = stream.getvalue().decode()
    return render(request, 'bill.html', context )

def tailorSlip(request):
    info=tailor.objects.all()
    x=datetime.date.today()
    tail={i.tailor_name:[] for i in info}
    for i in Order.objects.all():
        if i.order_received==x:
            tail[i.tailor_assigned].append(i)
    final={}
    for i in tail:
        if tail[i]:
            final[i]=tail[i]
    template_path='tailorslip.html'
    context={'tailor':final , 'date':x }
    res=HttpResponse(content_type='application/pdf')
    name=str(datetime.date.today())+ '_tailorslip'+'.pdf'
    res['Content-Disposition']='attachment; filename={} '.format(name)
    temp=get_template(template_path)
    htm=temp.render(context)
    pisa_status=pisa.CreatePDF( htm, dest=res)
    return res

def Tailors(request):
    info=tailor.objects.all()
    tail={ i.tailor_name:[] for i in info}
    sno=[]
    sno=[i.serial_no for i in info]
    for i in Order.objects.all():
        tail[i.tailor_assigned].append(i)
    for key,value in tail.items():
        value.sort(key= lambda x: x.order_received, reverse=True)
    context={'tailor':tail, 'serial': sno, 'data':info}
    return render(request,'tailors.html',context)


def OrderReceivedSlip(request):
    now=[]
    x=datetime.date.today()
    for i in Order.objects.all():
        if i.order_received==x: now.append(i)
    template_path='ReceivedSlip.html'
    context={'today':now, 'date':x}
    res=HttpResponse(content_type='application/pdf')
    name=str(datetime.date.today())+ '_Receivedslip'+'.pdf'
    res['Content-Disposition']='attachment; filename={} '.format(name)
    temp=get_template(template_path)
    htm=temp.render(context)
    pisa_status=pisa.CreatePDF( htm, dest=res)
    return res

def OrderCompletedSlip(request):
    now=[]
    x=datetime.date.today()
    for i in Completed.objects.all():
        if i.order_completed==x: now.append(i)
    template_path='doneslip.html'
    context={'today':now,'date':x}
    res=HttpResponse(content_type='application/pdf')
    name=str(datetime.date.today())+ '_Completedslip'+'.pdf'
    res['Content-Disposition']='attachment; filename={} '.format(name)
    temp=get_template(template_path)
    htm=temp.render(context)
    pisa_status=pisa.CreatePDF( htm, dest=res)
    return res

def Completedorders(request):
    x=Completed.objects.all().order_by('-order_completed')
    context={'pend':x}
    if request.method=='POST':
        y=request.POST.get("inp")
        if y:
            li=[]
            for i in Completed.objects.all():
                if i.serial_number.startswith(y) or i.mobile_number.startswith(y):
                    li.append(i)
            context={"pend":li}
            return render(request, 'complete.html',context)
    return render(request,'complete.html',context)


def EditTailor(request, tid):
    old=tailor.objects.get(tailorid=tid)
    form=tailors(instance=old)
    if request.method=='POST':
        form=tailors(request.POST)
        if form.is_valid():
            old.delete()
            tailor1=form.save(commit=False)
            tailor1.tailor_name=tailor1.tailor_name.upper()
            
            tailor1.save()
            messages.success(request,'Details Edited Successfully!')
            return redirect('/')
    return render(request,'addtailor.html',{'form':form})

def EditOrder(request,oid):
    global order
    old=Order.objects.get(Order_id=oid)
    form=OrderForm(instance=old)
    if request.method=='POST':
        form=OrderForm(request.POST, instance=old)
        if form.is_valid():
            order.remove(old)
            old.delete()
            orde=form.save(commit=False)
            orde.tailor_assigned=orde.tailor_assigned.upper()
            order.append(orde)
            orde.save()
            messages.success(request,'Details Edited Successfully!')
            return redirect('/')
    return render(request,'addorder.html',{'form':form})

def view_404(request, exception=None):
    x=str(request).split('/')[-2]
    url='/'+x
    return redirect(url)
