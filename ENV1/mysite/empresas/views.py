from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from empresas.models import Empresas, Valoracion


# Create your views here.
def index (request):
	lista_ultimas_empresas = Empresas.objects.all()
	context = {'lista_ultimas_empresas': lista_ultimas_empresas}
	return render(request, 'empresas/index.html', context)

	
def datos (request, empresa_id):
	#empresa = get_object_or_404 (Empresas, pk=empresa_id)
	empresa=Empresas.objects.get(pk=empresa_id)
	return render(request, 'empresas/datos.html', {'empresa': empresa})

	
def valoraciones (request, empresa_id):
	todos_valoraciones=Valoracion.objects.all().filter(empresa=empresa_id)
	context2 = {'todos_valoraciones':todos_valoraciones}
	return render(request, 'empresas/valoraciones.html', context2)
	
def puntuaciones (request, empresa_id):
	empresa = Empresas.objects.get(pk=empresa_id)
	puntuaciones_empresa = Valoracion.objects.filter(empresa=empresa)
	context3 = {'puntuaciones_empresa':puntuaciones_empresa}
	#puntuacion=Valoracion.objects.get(pk=empresa_id)
	return render(request, 'empresas/puntuaciones.html', context3)
	
	
from empresas.forms import EmpresasForm

def add_empresa(request):
    # A HTTP POST?
	if request.method == 'POST':
		form = EmpresasForm(request.POST)

        # Have we been provided with a valid form?
		if form.is_valid():
            # Save the new category to the database.
			form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
			return index(request)
		else:
            # The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
        # If the request was not a POST, display the form to enter details.
		form = EmpresasForm()

	# Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
	return render(request, 'empresas/add_empresa.html', {'form': form})

	



