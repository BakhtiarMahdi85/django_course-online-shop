from django.shortcuts import render
from django.views import generic
# from accounts.form import CustomUserCreationForm
#
class HomePageView(generic.TemplateView):
    template_name = 'Homepage.html'

class AboutUsView(generic.TemplateView):
    template_name = 'pages/aboutus.html'


