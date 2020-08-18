from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'

class LoggedinPage(TemplateView):
    template_name = 'loggedin.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
