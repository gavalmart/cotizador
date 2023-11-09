from django.test import TestCase
from django.urls import reverse
from .models import Capacidad
from .models import Proveedor
from .models import HistorialCompras

# Create your tests here.

class CapacidadTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.capacidad = Capacidad.objects.create(valor=20, unidadMedida='TB', activo=True)

    def test_model_content(self):
        self.assertEqual(self.capacidad.valor,20)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/capacidades/")
        self.assertEqual(response.status_code,200)

    def test_homepage(self):
        response = self.client.get(reverse('listar_capacidad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "capacidades/cap_listar.html")
        self.assertContains(response, 20)


class ProveedorTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.capacidad = Capacidad.objects.create(valor=20, unidadMedida='TB', activo=True)

    def test_model_content(self):
        self.assertEqual(self.capacidad.valor,20)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/capacidades/")
        self.assertEqual(response.status_code,200)

    def test_homepage(self):
        response = self.client.get(reverse('listar_capacidad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "capacidades/cap_listar.html")
        self.assertContains(response, 20)
