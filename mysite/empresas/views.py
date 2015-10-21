from django.shortcuts import render

from django.http import HttpResponse
import datetime 
import sqlite3 

# Create your views here.

INSTALLED_APPS = (
# ...
'mysite.empresas',
# ...
)


def index(request):
	crear_empresa('nombre_e','correo_e'):
    return HttpResponse("Hello, world. You're at the poll index.")
#funcion para tontear con las vistas

def crear_empresa(nombre_e,correo_e):
	conn=sqlite3.connect('test.db')
	c.execute('INSERT INTO Empresas VALUES (hugo,correo)')




def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
