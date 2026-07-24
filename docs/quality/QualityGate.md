# Quality Gate - Evidencias
## Proyecto: QA Student Tracker

---

## Configuración del Gate

El workflow `quality-gate.yml` se ejecuta automáticamente en cada Pull Request hacia `main`.

**Criterios validados:**

| # | Criterio | Herramienta | Resultado esperado |
|---|---|---|---|
| 1 | Existencia de `README.md` | bash `test -f` | Exit code 0 |
| 2 | Existencia de `docs/quality/CTQ.md` | bash `test -f` | Exit code 0 |
| 3 | Existencia de `docs/quality/DoD.md` | bash `test -f` | Exit code 0 |
| 4 | Contenido mínimo en CTQ.md (contiene "CTQ") | `grep -q` | Exit code 0 |
| 5 | Contenido mínimo en DoD.md (contiene "Definition of Done") | `grep -q` | Exit code 0 |
| 6 | Linter sin errores críticos | `flake8` E9,F63,F7,F82 | 0 errores |
| 7 | Pruebas unitarias pasando | `pytest` | Exit code 0 |

---

## Limitaciones conocidas

> **Regla de protección de rama:** GitHub requiere cuenta Team u Organización para configurar status checks obligatorios en `main`. Con cuenta gratuita, la ejecución del gate es visible en GitHub Actions pero no bloquea automáticamente el merge. Se documenta esta limitación como evidencia válida según las instrucciones de la actividad.

---

## Registro de ejecuciones

> _Completar esta sección con los enlaces reales una vez ejecutado el PR._

| Fecha | PR | Resultado | Enlace Actions | Observaciones |
|---|---|---|---|---|
| 2026-07-23 | #1 feature/quality-baseline → main | ✅ Passed | [Ver run](https://github.com/JFigueroatz/qa-student-tracker/actions/runs/30017301343/job/89240531964?pr=1) | Ejecución inicial — 16 tests passed, 0 errores flake8 |

---

## Conclusión del Sprint

| Ítem | Estado |
|---|---|
| CTQs Must completados | ✅ 3/3 |
| Issues cerrados | ✅ 3/3 |
| PR aprobado | ✅ AndreaChk |
| Gate ejecutado | ✅ 13 segundos |
| Pruebas unitarias | ✅ 16/16 passed |
| Errores de linter | ✅ 0 errores |

## Cómo interpretar el resultado

- ✅ **Passed:** Todos los pasos del job `quality-gate` completaron con exit code 0. El PR puede fusionarse.
- ❌ **Failed:** Al menos un paso falló. El PR **no debe fusionarse** hasta documentar la causa y resolverla o justificarla como excepción DoD.
