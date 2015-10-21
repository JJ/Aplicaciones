from django.test import TestCase

# Create your tests here.

from empresas.models import Empresas

class EmpresasMethodTests(TestCase):

	def test_nombre_empresa(self):
		emp = Empresas(nombre='test',correo='ctest')
		emp.save()
		self.assertEqual(emp.nombre, 'empresa')
