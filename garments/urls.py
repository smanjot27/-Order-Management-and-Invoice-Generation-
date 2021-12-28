from garments import views
from django.contrib import admin
from django.urls import path,include, re_path
import re
#handler404 = 'garments.views.view_404'
urlpatterns = [
    path('', views.FullDaySales),
    path('fullday',views.FullDaySales),
    path('orders', views.OrderDetails),
    path('tailors',views.Tailors),
    path('neworder', views.AddOrder),
    path('newtailor', views.Addtailor),
    path('pendingorders', views.Pending),
    path('generatebill/<str:serial_no>', views.GenerateBill),
    path('tailorSlip', views.tailorSlip),
    path('receivedslip', views.OrderReceivedSlip),
    path('completedslip', views.OrderCompletedSlip),
    path('completedorders', views.Completedorders),
    path('edittailors/<int:tid>', views.EditTailor),
    path('editorder/<int:oid>', views.EditOrder),
    re_path('^edit.*/$', views.view_404)
]

