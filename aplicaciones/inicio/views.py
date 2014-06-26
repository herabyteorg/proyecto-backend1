from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class index(TemplateView):
	template_name = 'inicio/index.html'

class test(TemplateView):
	template_name = 'inicio/testview.html'


"""def index(request):
	return render_to_response('inicio/index.html')"""