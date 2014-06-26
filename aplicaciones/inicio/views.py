from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('index.html')
	html = t.render(Context({'current_datetime': now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>En %s hora(s), seran las %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

