from django.shortcuts import render
from .models import Contact,Category, Portfolio, About,Resume,Services
from django.views.generic.edit import FormView
from .bot import send_message
from django.views.generic.list import ListView
from django.views import View

class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        # country = request.POST.get('country')
        # subject = request.POST.get('subject')
        message = request.POST.get('message')  

        # Save contact info in the database
        contact = Contact(
            name=name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        contact.save()

        message_text = f"New Contact Form Submission:\n\nFirst Name: {name}\nPhone_number: {phone_number}\nEmail: {email}"

        send_message(message_text)

        print("Siz Post request yubordingiz")

        return render(request, self.template_name)

def home_view(request):
    return render(request=request, template_name='hero.html')


class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about' 

class ResumeListView(ListView):
    model = Resume
    template_name = 'resume.html'
    context_object_name = 'resume' 

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolio' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
        return context 

class ServicesListView(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'services' 
