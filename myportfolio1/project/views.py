from django.http import HttpResponse
from django.template import loader

def project(request):
  template = loader.get_template('project.html')
  return HttpResponse(template.render())