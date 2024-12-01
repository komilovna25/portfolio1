from django.contrib import admin
from .models import Contact, About, Portfolio
from .forms import ContactForm

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'message']
    readonly_fields = ['id']


    form = ContactForm

admin.site.register(Contact, ContactAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    

admin.site.register(About, AboutAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    

admin.site.register(Portfolio, PortfolioAdmin)
