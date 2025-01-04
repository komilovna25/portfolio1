from django.contrib import admin
from .models import Contact, About, Category,Portfolio,Services
from .forms import ContactForm
from django.utils.html import format_html


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    readonly_fields = ['id']
     
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','message')
    readonly_fields = ['id']
     

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

