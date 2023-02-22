import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates,'
)

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
    
    def project(request):
          pass


