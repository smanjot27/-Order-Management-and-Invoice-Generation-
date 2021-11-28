from django.contrib import admin
from garments.models import Order, tailor, Completed

admin.site.register(Order)
admin.site.register(tailor)
admin.site.register(Completed)

# Register your models here.
