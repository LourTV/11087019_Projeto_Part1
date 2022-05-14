from django.contrib import admin
from .models import Payment, Films, Session, Costumer

admin.site.register(Payment)
admin.site.register(Films)
admin.site.register(Session)
admin.site.register(Costumer)

# Register your models here.
