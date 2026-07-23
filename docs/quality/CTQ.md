# Matriz CTQ - Critical to Quality
## Proyecto: QA Student Tracker

---

## Tabla CTQ

| ID | Necesidad del usuario/negocio | CTQ | Métrica | Umbral aceptable | Evidencia | Prioridad | Issue |
|---|---|---|---|---|---|---|---|
| CTQ-001 | El docente necesita saber con certeza si una entrega es válida o no, sin ambigüedad | Validación confiable de entregas | % de casos de validación con resultado correcto en pruebas | >= 95% de pruebas pasando | `pytest src/test_tracker.py -v` + resultado en GitHub Actions | Must | #1 |
| CTQ-002 | El sistema debe procesar listas de notas y calcular promedios sin errores de redondeo ni fallas silenciosas | Exactitud en cálculo de promedios | % de cálculos con resultado correcto al 2do decimal | 100% en casos de prueba definidos | Test `TestCalcularPromedio` en GitHub Actions | Must | #2 |
| CTQ-003 | El código debe ser mantenible y legible para que cualquier integrante pueda continuarlo sin fricción | Calidad estática del código | Número de errores críticos reportados por flake8 (E9, F63, F7, F82) | 0 errores bloqueantes | Ejecución de `flake8` en GitHub Actions | Must | #3 |

---

## Reglas de trazabilidad

- Cada CTQ tiene un issue asociado en el GitHub Project.
- Cada issue incluye la evidencia esperada y el responsable.
- Ningún CTQ con prioridad **Must** puede cerrarse sin cumplir el DoD completo.
- El ID del CTQ debe aparecer en el PR que lo resuelve.

---

## Mapa de trazabilidad

```
CTQ-001 → Issue #1 → TestValidarEntrega → quality-gate.yml → PR #1
CTQ-002 → Issue #2 → TestCalcularPromedio → quality-gate.yml → PR #1
CTQ-003 → Issue #3 → flake8 src/ → quality-gate.yml → PR #1
```

---

## Historial de cambios

| Versión | Fecha | Cambio | Responsable |
|---|---|---|---|
| 1.0 | 2026-07-23 | Creación inicial de la matriz | Jefferson Tzib |
