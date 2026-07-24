"""
Pruebas unitarias para qa-student-tracker.
Ejecutar con: pytest src/test_tracker.py -v
"""
import pytest
from tracker import calcular_promedio, estado_estudiante, validar_entrega


# ── CTQ-001: Validación de entrega ──────────────────────────────────────────

class TestValidarEntrega:
    def test_entrega_aprobada(self):
        resultado = validar_entrega("Actividad 1", 85.0, True)
        assert resultado["estado"] == "aprobado"

    def test_entrega_reprobada_por_nota(self):
        resultado = validar_entrega("Actividad 2", 50.0, True)
        assert resultado["estado"] == "reprobado"

    def test_entrega_reprobada_por_tiempo(self):
        resultado = validar_entrega("Actividad 3", 90.0, False)
        assert resultado["estado"] == "reprobado"

    def test_nombre_vacio_retorna_error(self):
        resultado = validar_entrega("", 75.0, True)
        assert resultado["estado"] == "error"

    def test_nota_fuera_de_rango(self):
        resultado = validar_entrega("Actividad 4", 110.0, True)
        assert resultado["estado"] == "error"

    def test_nota_minima_aprobatoria(self):
        resultado = validar_entrega("Actividad 5", 61.0, True)
        assert resultado["estado"] == "aprobado"


# CTQ-002: Cálculo de promedio

class TestCalcularPromedio:
    def test_promedio_normal(self):
        assert calcular_promedio([80, 90, 70]) == 80.0

    def test_lista_vacia_retorna_cero(self):
        assert calcular_promedio([]) == 0.0

    def test_promedio_con_decimales(self):
        assert calcular_promedio([100, 75, 88]) == 87.67

    def test_promedio_un_elemento(self):
        assert calcular_promedio([95]) == 95.0


# CTQ-003: Estado del estudiante 

class TestEstadoEstudiante:
    def test_excelente(self):
        assert estado_estudiante(95) == "Excelente"

    def test_satisfactorio(self):
        assert estado_estudiante(80) == "Satisfactorio"

    def test_aprobado(self):
        assert estado_estudiante(65) == "Aprobado"

    def test_reprobado(self):
        assert estado_estudiante(50) == "Reprobado"

    def test_limite_aprobado(self):
        assert estado_estudiante(61) == "Aprobado"

    def test_limite_excelente(self):
        assert estado_estudiante(90) == "Excelente"
